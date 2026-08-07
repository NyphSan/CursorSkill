#Requires -Version 5.1
<#
.SYNOPSIS
  Optimize local network for stable Cursor (Agent / Task / GPT).
  Locks: v2ray up, Global routing, system+Cursor HTTP proxy 10809, env proxy, netcheck gate.
#>
param(
  [string]$V2rayRoot = "C:\Users\as353\Desktop\VPN\v2rayN-windows-64",
  [int]$HttpPort = 10809,
  [int]$SocksPort = 10808,
  [switch]$SkipRouting,
  [switch]$SkipCursorSettings
)

$ErrorActionPreference = "Continue"
$failed = @()
Write-Host "=== optimize-cursor-network ===" -ForegroundColor Cyan

# 1) Ensure v2ray
$ensure = "E:\dev\CursorTeam\scripts\ensure-v2ray.ps1"
if (Test-Path $ensure) {
  # temp patch behavior: we'll set proxy ourselves to HTTP port
  & powershell -ExecutionPolicy Bypass -File $ensure
} else {
  Write-Host "WARN ensure-v2ray.ps1 missing" -ForegroundColor Yellow
}

# 2) Global routing
if (-not $SkipRouting) {
  $route = "E:\dev\CursorTeam\scripts\v2rayn-set-routing.ps1"
  if (Test-Path $route) {
    Write-Host "Ensuring Global routing..."
    & powershell -ExecutionPolicy Bypass -File $route -Mode Global -NoRestart
  }
}

# 3) Wait for HTTP inbound
$httpOk = $false
for ($i = 0; $i -lt 20; $i++) {
  if (Get-NetTCPConnection -LocalPort $HttpPort -State Listen -ErrorAction SilentlyContinue) { $httpOk = $true; break }
  Start-Sleep -Seconds 1
}
if (-not $httpOk) {
  Write-Host "WARN: HTTP $HttpPort not listening — enable v2rayN mixed/extra HTTP port" -ForegroundColor Yellow
  $failed += "http-port"
} else {
  Write-Host "OK: HTTP $HttpPort listening" -ForegroundColor Green
}

# 4) System proxy -> HTTP (not SOCKS)
$ie = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
$want = "127.0.0.1:$HttpPort"
Set-ItemProperty $ie -Name ProxyEnable -Value 1
Set-ItemProperty $ie -Name ProxyServer -Value $want
# bypass local
$bypass = "localhost;127.*;10.*;172.16.*;172.17.*;172.18.*;172.19.*;172.20.*;172.21.*;172.22.*;172.23.*;172.24.*;172.25.*;172.26.*;172.27.*;172.28.*;172.29.*;172.30.*;172.31.*;192.168.*"
Set-ItemProperty $ie -Name ProxyOverride -Value $bypass -ErrorAction SilentlyContinue
Write-Host "System proxy -> $want"

# 5) User env proxy for CLI / Node children
$proxyUrl = "http://127.0.0.1:$HttpPort"
[Environment]::SetEnvironmentVariable("HTTP_PROXY", $proxyUrl, "User")
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", $proxyUrl, "User")
[Environment]::SetEnvironmentVariable("http_proxy", $proxyUrl, "User")
[Environment]::SetEnvironmentVariable("https_proxy", $proxyUrl, "User")
[Environment]::SetEnvironmentVariable("NO_PROXY", "localhost,127.0.0.1", "User")
$env:HTTP_PROXY = $proxyUrl
$env:HTTPS_PROXY = $proxyUrl
$env:http_proxy = $proxyUrl
$env:https_proxy = $proxyUrl
Write-Host "User env HTTP(S)_PROXY -> $proxyUrl"

# 6) Cursor settings.json
if (-not $SkipCursorSettings) {
  $settingsPath = Join-Path $env:APPDATA "Cursor\User\settings.json"
  if (Test-Path $settingsPath) {
    try {
      $j = Get-Content $settingsPath -Raw -Encoding UTF8 | ConvertFrom-Json
      $j | Add-Member -NotePropertyName "http.proxySupport" -NotePropertyValue "on" -Force
      $j | Add-Member -NotePropertyName "http.systemCertificates" -NotePropertyValue $true -Force
      $j | Add-Member -NotePropertyName "cursor.general.disableHttp2" -NotePropertyValue $true -Force
      $j | Add-Member -NotePropertyName "http.proxy" -NotePropertyValue $proxyUrl -Force
      ($j | ConvertTo-Json -Depth 20) | Set-Content $settingsPath -Encoding UTF8
      Write-Host "Cursor settings: proxy=$proxyUrl disableHttp2=true"
    } catch {
      Write-Host "WARN Cursor settings patch failed: $($_.Exception.Message)" -ForegroundColor Yellow
      $failed += "cursor-settings"
    }
  }
}

# 7) Netcheck gate
function Test-Url([string]$Url, [string]$Proxy) {
  $out = & curl.exe -sS -o NUL -w "code=%{http_code}" --proxy $Proxy --connect-timeout 12 --max-time 20 $Url 2>&1 | Out-String
  if ($out -match "HTTP/0\.9") { return @{ ok = $false; detail = "HTTP/0.9" } }
  if ($out -match "code=(200|401|403|404)") { return @{ ok = $true; detail = $Matches[0] } }
  return @{ ok = $false; detail = $out.Trim() }
}

$proxyArg = "http://127.0.0.1:$HttpPort"
if (-not $httpOk) { $proxyArg = "socks5h://127.0.0.1:$SocksPort" }

Write-Host ""
Write-Host "=== connectivity gate ===" -ForegroundColor Cyan
$api2 = Test-Url "https://api2.cursor.sh/" $proxyArg
$agentn = Test-Url "https://agentn.global.api5.cursor.sh/" $proxyArg
$oai = Test-Url "https://api.openai.com/v1/models" $proxyArg

Write-Host ("api2    : {0} ({1})" -f $(if ($api2.ok) { "OK" } else { "FAIL" }), $api2.detail)
Write-Host ("agentn  : {0} ({1})" -f $(if ($agentn.ok) { "OK" } else { "FAIL" }), $agentn.detail)
Write-Host ("openai  : {0} ({1})" -f $(if ($oai.ok) { "OK" } else { "FAIL" }), $oai.detail)

if (-not $api2.ok) { $failed += "api2" }
if (-not $agentn.ok) { $failed += "agentn" }

# 8) Report
$reportDir = "E:\dev\CursorTeam\docs\network"
New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$report = Join-Path $reportDir ("NETOPT-{0}.md" -f $stamp)
@"
# NETOPT $stamp

| Item | Value |
|------|-------|
| HTTP proxy | 127.0.0.1:$HttpPort |
| SOCKS | 127.0.0.1:$SocksPort |
| Routing | Global (requested) |
| api2 | $($api2.detail) |
| agentn | $($agentn.detail) |
| openai | $($oai.detail) |
| failed | $($failed -join ', ') |

## Boss action if agentn FAIL
1. v2rayN switch node
2. Re-run: powershell -File E:\dev\CursorTeam\scripts\optimize-cursor-network.ps1
3. Until agentn OK — do not expect stable Task/GPT Agent
"@ | Set-Content $report -Encoding UTF8
Write-Host "Report: $report"

Write-Host ""
if ($failed -contains "agentn") {
  Write-Host "NOT STABLE YET: switch v2rayN NODE (agentn still broken)." -ForegroundColor Red
  Write-Host "Local proxy stack optimized; Cursor should use HTTP $HttpPort + HTTP/1.1."
  exit 4
}
if ($failed.Count -gt 0) {
  Write-Host ("PARTIAL: {0}" -f ($failed -join ', ')) -ForegroundColor Yellow
  exit 5
}
Write-Host "STABLE GATE PASS: api2+agentn OK. Restart Cursor, then retry Task." -ForegroundColor Green
exit 0
