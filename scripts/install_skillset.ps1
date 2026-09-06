#Requires -Version 5.1
<#
.SYNOPSIS
Installs a professional AgentCannabis skillset for Copilot in a Git project.
.DESCRIPTION
Validates skillsets/<name>.json and its declared local skill paths before
installing from GitHub. By default only the self-contained wrapper is installed.
Use -IncludeMembers to also expose each atomic skill for direct invocation.
.EXAMPLE
./scripts/install_skillset.ps1 -Skillset cultivation-technician -ProjectPath D:/MyProject -WhatIf
.EXAMPLE
./scripts/install_skillset.ps1 -Skillset cultivation-technician -ProjectPath D:/MyProject -Ref TAG -Pin
#>
[CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'Low')]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[a-z0-9]+(?:-[a-z0-9]+)*$')]
    [ValidateLength(1, 64)]
    [string]$Skillset,

    [ValidateNotNullOrEmpty()]
    [string]$ProjectPath = (Get-Location).Path,

    [ValidatePattern('^[A-Za-z0-9][A-Za-z0-9._/-]*$')]
    [string]$Ref = 'main',

    [switch]$Pin,
    [switch]$IncludeMembers
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$sourceRepository = 'jeremylongworth-source/AgentCannabis'
$sourceRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$sourcePrefix = $sourceRoot.TrimEnd([IO.Path]::DirectorySeparatorChar) + [IO.Path]::DirectorySeparatorChar

function Assert-SkillName {
    param([object]$Value)
    if ($Value -isnot [string] -or $Value.Length -gt 64 -or
        $Value -cnotmatch '^[a-z0-9]+(?:-[a-z0-9]+)*$') {
        throw 'Manifest skill names must be 1-64 lowercase letters, numbers, and single hyphens; paths are not accepted.'
    }
}

function Get-RepositoryFile {
    param([string]$RelativePath)
    $candidate = [IO.Path]::GetFullPath((Join-Path $sourceRoot $RelativePath))
    if (-not $candidate.StartsWith($sourcePrefix, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Repository path escapes the source repository: $RelativePath"
    }
    if (-not (Test-Path -LiteralPath $candidate -PathType Leaf)) {
        throw "Required repository file is missing: $RelativePath"
    }
    # A declared skill cannot redirect reads outside the repository through a link.
    $currentItem = Get-Item -LiteralPath $candidate -Force
    while ($null -ne $currentItem -and $currentItem.FullName -ne $sourceRoot) {
        if (($currentItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw "Linked files or directories are not accepted: $RelativePath"
        }
        $currentItem = Get-Item -LiteralPath (Split-Path -Parent $currentItem.FullName) -Force
    }
    return $candidate
}

Assert-SkillName $Skillset
if ($Ref.Contains('..') -or $Ref.Contains('//') -or $Ref.EndsWith('/') -or $Ref.EndsWith('.')) {
    throw 'Ref must be main, a release tag, or a commit SHA without traversal or empty path components.'
}
if ($Pin -and $Ref -eq 'main') {
    throw 'Use -Pin with a reviewed release tag or commit SHA, not the moving main branch.'
}

$manifestPath = Get-RepositoryFile "skillsets/$Skillset.json"
$manifest = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
if ($null -eq $manifest -or $null -eq $manifest.PSObject.Properties['name'] -or
    $null -eq $manifest.PSObject.Properties['included_skills']) {
    throw 'The skillset manifest must contain name and included_skills.'
}
Assert-SkillName $manifest.name
if ($manifest.name -cne $Skillset) {
    throw "Manifest name does not match skillsets/$Skillset.json."
}
if ($manifest.included_skills -isnot [Array] -or $manifest.included_skills.Count -eq 0) {
    throw 'included_skills must be a nonempty JSON array of atomic skill names.'
}

$seen = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($member in $manifest.included_skills) {
    Assert-SkillName $member
    if ($member -ceq $Skillset -or -not $seen.Add($member)) {
        throw "Manifest contains a duplicate member or includes its own wrapper: $member"
    }
    $null = Get-RepositoryFile "skills/$member/SKILL.md"
}
$null = Get-RepositoryFile "skills/$Skillset/SKILL.md"
$selectedSkills = @($Skillset)
if ($IncludeMembers) {
    $selectedSkills += @($manifest.included_skills)
}

$gitCommand = Get-Command git -CommandType Application -ErrorAction Stop | Select-Object -First 1
$ghCommand = Get-Command gh -CommandType Application -ErrorAction Stop | Select-Object -First 1
$targetProject = (Resolve-Path -LiteralPath $ProjectPath -ErrorAction Stop).Path
if (-not (Test-Path -LiteralPath $targetProject -PathType Container)) {
    throw 'ProjectPath must be an existing directory in the destination Git project.'
}
$gitRootOutput = & $gitCommand.Source -C $targetProject rev-parse --show-toplevel
if ($LASTEXITCODE -ne 0 -or -not $gitRootOutput) {
    throw 'ProjectPath must belong to a Git worktree that Git can read. No Git trust settings were changed.'
}
$targetRoot = [IO.Path]::GetFullPath(($gitRootOutput | Select-Object -Last 1).Trim())

Write-Output "Manifest: $manifestPath"
Write-Output "Destination: $(Join-Path $targetRoot '.agents/skills')"
Write-Output "Source: $sourceRepository at $Ref"
Write-Output 'Use a local manifest from the same revision as the remote ref when installing members.'

Push-Location -LiteralPath $targetRoot
try {
    foreach ($selectedSkill in $selectedSkills) {
        $remotePath = "skills/$selectedSkill"
        if ($Pin) {
            $ghArguments = @('skill', 'install', $sourceRepository, $remotePath, '--pin', $Ref,
                '--agent', 'github-copilot', '--scope', 'project')
        }
        else {
            $ghArguments = @('skill', 'install', $sourceRepository, "$remotePath@$Ref",
                '--agent', 'github-copilot', '--scope', 'project')
        }
        Write-Output ('gh ' + ($ghArguments -join ' '))
        if ($PSCmdlet.ShouldProcess($targetRoot, "Install $selectedSkill from $sourceRepository at $Ref")) {
            & $ghCommand.Source @ghArguments
            if ($LASTEXITCODE -ne 0) {
                throw "gh skill install failed for $selectedSkill (exit $LASTEXITCODE). Earlier successful installs remain in place; inspect them before retrying."
            }
        }
    }
}
finally {
    Pop-Location
}
