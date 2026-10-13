$root = Resolve-Path (Join-Path $PSScriptRoot '..')
$file = Join-Path $root 'logs\status.json'
if (-not (Test-Path $file)) { Write-Host 'No status file yet'; exit 1 }
Get-Content $file -Raw
