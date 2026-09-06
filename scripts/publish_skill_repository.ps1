#Requires -Version 5.1
<#+
.SYNOPSIS
Runs gh skill publish with a scoped Git safe.directory override.
.DESCRIPTION
GitHub CLI 2.92.0 shells out to Git during gh skill publish. On Windows, a
Codex-created checkout can have .git ownership that differs from the interactive
user, which causes Git to report dubious ownership. This wrapper scopes the
safe.directory trust decision to the current gh process instead of writing to
user-level global Git config.
#>
param(
  [string]$Directory = '',
  [switch]$DryRun,
  [string]$Tag = ''
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($Directory)) {
  $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
  $Directory = (Resolve-Path (Join-Path $scriptDir '..')).Path
} else {
  $Directory = (Resolve-Path -LiteralPath $Directory).Path
}

$safeDirectory = $Directory.Replace('\\', '/')
$ghArgs = @('skill', 'publish', $Directory)
if ($DryRun) {
  $ghArgs += '--dry-run'
}
if (-not [string]::IsNullOrWhiteSpace($Tag)) {
  $ghArgs += @('--tag', $Tag)
}

$originalGitConfigEnv = @{}
Get-ChildItem Env:GIT_CONFIG_* -ErrorAction SilentlyContinue | ForEach-Object {
  $originalGitConfigEnv[$_.Name] = $_.Value
}

try {
  $existingCount = 0
  if ($env:GIT_CONFIG_COUNT -match '^\d+$') {
    $existingCount = [int]$env:GIT_CONFIG_COUNT
  }
  $index = $existingCount
  Set-Item -Path "Env:GIT_CONFIG_KEY_$index" -Value 'safe.directory'
  Set-Item -Path "Env:GIT_CONFIG_VALUE_$index" -Value $safeDirectory
  Set-Item -Path Env:GIT_CONFIG_COUNT -Value ([string]($existingCount + 1))

  gh @ghArgs
  exit $LASTEXITCODE
}
finally {
  Get-ChildItem Env:GIT_CONFIG_* -ErrorAction SilentlyContinue | ForEach-Object {
    Remove-Item -Path "Env:$($_.Name)" -ErrorAction SilentlyContinue
  }
  foreach ($entry in $originalGitConfigEnv.GetEnumerator()) {
    Set-Item -Path "Env:$($entry.Key)" -Value $entry.Value
  }
}
