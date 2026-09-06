$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot

python "$PSScriptRoot\validate_repository.py" --stage full
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-source-links.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python -m unittest discover -s "$RepoRoot\tests" -v
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host "All AgentCannabis validation checks passed."
