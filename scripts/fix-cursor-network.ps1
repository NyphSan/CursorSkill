#Requires -Version 5.1
<#
.SYNOPSIS
  Cursor / Task 子代理网络修复检查清单（自动能做的做完，节点切换须人手）
#>
param(
  [switch]$SetGlobalRouting
)

$ErrorActionPreference = "Continue"
Write-Host "=== fix-cursor-network ===" -ForegroundColor Cyan

# 1) proxy up
& powershell -ExecutionPolicy Bypass -File "E:\dev\CursorTeam\scripts\ensure-v2ray.ps1"
if ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne $null) {
  Write-Host "ensure-v2ray exit $LASTEXITCODE" -ForegroundColor Yellow
}

# 2) global routing
if ($SetGlobalRouting) {
  & powershell -ExecutionPolicy Bypass -File "E:\dev\CursorTeam\scripts\v2rayn-set-routing.ps1" -Mode Global
}

# 3) Cursor IDE settings
$settingsPath = Join-Path $env:APPDATA "Cursor\User\settings.json"
if (Test-Path $settingsPath) {
  $j = Get-Content $settingsPath -Raw -Encoding UTF8 | ConvertFrom-Json
  $changed = $false
  if (-not $j.'cursor.general.disableHttp2') {
    $j | Add-Member -NotePropertyName 'cursor.general.disableHttp2' -NotePropertyValue $true -Force
    $changed = $true
  }
  if ($j.'http.proxySupport' -ne 'on') {
    $j | Add-Member -NotePropertyName 'http.proxySupport' -NotePropertyValue 'on' -Force
    $changed = $true
  }
  if ($changed) {
    $j | ConvertTo-Json -Depth 20 | Set-Content $settingsPath -Encoding UTF8
    Write-Host "Updated Cursor settings.json (disableHttp2 + proxySupport)" -ForegroundColor Yellow
  } else {
    Write-Host "Cursor settings already OK (disableHttp2 + proxySupport)"
  }
}

# 4) TUN reality
$tunCfg = $false
try {
  $g = Get-Content "C:\Users\as353\Desktop\VPN\v2rayN-windows-64\guiConfigs\guiNConfig.json" -Raw -Encoding UTF8 | ConvertFrom-Json
  $tunCfg = [bool]$g.TunModeItem.EnableTun
} catch {}
$tunAdapter = Get-NetAdapter -IncludeHidden -ErrorAction SilentlyContinue | Where-Object {
  $_.InterfaceDescription -match 'Wintun|Meta|sing-box|TUN' -or $_.Name -match 'tun|meta'
}
Write-Host ("TUN config EnableTun={0}" -f $tunCfg)
if ($tunAdapter) {
  Write-Host ("TUN adapter: {0} Status={1}" -f $tunAdapter[0].Name, $tunAdapter[0].Status) -ForegroundColor Green
} else {
  Write-Host "TUN adapter: NOT PRESENT (config may say on, but driver not up — restart v2rayN as Admin)" -ForegroundColor Red
}

# 5) endpoint tests
Write-Host ""
& powershell -ExecutionPolicy Bypass -File "E:\dev\CursorTeam\scripts\cursor-gpt-netcheck.ps1"

Write-Host ""
Write-Host "=== Manual steps YOU must do if agentn still FAIL ===" -ForegroundColor Yellow
Write-Host "1) v2rayN: right-click tray -> Run as Administrator, enable TUN again"
Write-Host "2) Switch server/node; after EACH node run:"
Write-Host "   powershell -File E:\dev\CursorTeam\scripts\cursor-gpt-netcheck.ps1"
Write-Host "3) Stop when [SOCKS-agentn] is OK (not HTTP/0.9)"
Write-Host "4) Restart Cursor IDE completely"
Write-Host "5) Then re-dispatch ARCH-F4c Task"
