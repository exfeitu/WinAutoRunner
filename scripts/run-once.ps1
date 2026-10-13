$ErrorActionPreference = 'Stop'
Set-Location (Resolve-Path (Join-Path $PSScriptRoot '..'))
& .\.venv\Scripts\python.exe src\runner.py --once
exit $LASTEXITCODE
