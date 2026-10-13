$ErrorActionPreference = 'Stop'
Set-Location (Resolve-Path (Join-Path $PSScriptRoot '..'))
while ($true) {
  & .\.venv\Scripts\python.exe src\runner.py
  Write-Warning "Runner exited with code $LASTEXITCODE; retrying in 15 seconds"
  Start-Sleep -Seconds 15
}
