# Deliberately does not configure auto-logon. Run at an already signed-in user's desktop.
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$target = Join-Path $root 'scripts\run-loop.ps1'
$startup = [Environment]::GetFolderPath('Startup')
$shortcutPath = Join-Path $startup 'WinAutoRunner.lnk'
$ws = New-Object -ComObject WScript.Shell
$shortcut = $ws.CreateShortcut($shortcutPath)
$shortcut.TargetPath = 'powershell.exe'
$shortcut.Arguments = '-NoProfile -ExecutionPolicy Bypass -File "' + $target + '"'
$shortcut.WorkingDirectory = $root
$shortcut.Save()
Write-Host "Created user startup shortcut: $shortcutPath"
Write-Host 'IMPORTANT: Requires an interactive desktop login. It does NOT enable auto-logon or prove RDP reliability.'
