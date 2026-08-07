#Requires -Version 5.1
<#
.SYNOPSIS
  Ensure v2rayN/xray is running; prefer HTTP inbound 10809 for system proxy.
#>
param(
  [string]$V2rayNExe = "C:\Users\as353\Desktop\VPN\v2rayN-windows-64\v2rayN.exe",
  [int]$SocksPort = 10808,
  [int]$HttpPort = 10809,
  [switch]$RunNetcheck
)

$ErrorActionPreference = "Continue"
Write-Host "=== ensure-v2ray ===" -ForegroundColor Cyan

if (-not (Test-Path $V2rayNExe)) {
  Write-Host "FAIL: v2rayN.exe not found: $V2rayNExe" -ForegroundColor Red
  exit 2
}

$v2 = Get-Process v2rayN -ErrorAction SilentlyContinue
if (-not $v2) {
  Write-Host "Starting v2rayN..."
  Start-Process -FilePath $V2rayNExe -WorkingDirectory (Split-Path $V2rayNExe)
  Start-Sleep -Seconds 4
} else {
  Write-Host ("v2rayN already running pid={0}" -f $v2.Id)
}

$ok = $false
for ($i = 0; $i -lt 20; $i++) {
  $socks = Get-NetTCPConnection -LocalPort $SocksPort -State Listen -ErrorAction SilentlyContinue
  $xray = Get-Process xray -ErrorAction SilentlyContinue
  if ($socks -and $xray) { $ok = $true; break }
  Start-Sleep -Seconds 1
}
if (-not $ok) {
  Write-Host ("FAIL: port {0} not listening / xray not up" -f $SocksPort) -ForegroundColor Red
  exit 3
}
Write-Host ("OK: core listening SOCKS {0}" -f $SocksPort) -ForegroundColor Green

$httpListen = Get-NetTCPConnection -LocalPort $HttpPort -State Listen -ErrorAction SilentlyContinue
$iePath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
if ($httpListen) {
  $want = "127.0.0.1:$HttpPort"
  Write-Host ("OK: HTTP {0} listening — system proxy uses HTTP" -f $HttpPort) -ForegroundColor Green
} else {
  $want = "127.0.0.1:$SocksPort"
  Write-Host ("WARN: HTTP {0} missing — system proxy falls back to {1} (prefer enable mixed HTTP)" -f $HttpPort, $SocksPort) -ForegroundColor Yellow
}

Set-ItemProperty $iePath -Name ProxyEnable -Value 1
Set-ItemProperty $iePath -Name ProxyServer -Value $want
Write-Host ("System proxy -> {0}" -f $want)

if ($RunNetcheck) {
  & powershell -ExecutionPolicy Bypass -File "E:\dev\CursorTeam\scripts\cursor-gpt-netcheck.ps1"
  exit $LASTEXITCODE
}
exit 0
