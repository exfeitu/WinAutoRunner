$ErrorActionPreference = 'Stop'
Set-Location (Resolve-Path (Join-Path $PSScriptRoot '..'))
if (-not (Get-Command py -ErrorAction SilentlyContinue)) { throw 'Install Python 3.12 and py launcher first' }
py -3.12 -m venv .venv
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
Write-Host 'Install Google Chrome separately. Run scripts\run-once.ps1 to validate.'
