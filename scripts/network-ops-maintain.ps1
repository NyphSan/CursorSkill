#Requires -Version 5.1
<#
.SYNOPSIS
  Network-ops daily maintain entry (handbook: docs/ops/NETWORK_OPS_HANDBOOK.md).
  Detect → optimize user-level stack → sync WinHTTP if admin → preflight → report.
#>
param(
  [switch]$BossConfirmGpt,
  [switch]$SkipOptimize,
  [switch]$SkipWinHttp
)

$ErrorActionPreference = "Continue"
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$reportDir = "E:\dev\CursorTeam\docs\network"
New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
$report = Join-Path $reportDir ("MAINTAIN-{0}.md" -f $stamp)

function Is-Admin {
  $p = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
  return $p.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

Write-Host "=== network-ops-maintain ===" -ForegroundColor Cyan
Write-Host "Handbook: docs/ops/NETWORK_OPS_HANDBOOK.md"

$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("# MAINTAIN $stamp")
$lines.Add("")
$lines.Add("- AdminShell: $(Is-Admin)")
$lines.Add("- Handbook: docs/ops/NETWORK_OPS_HANDBOOK.md")
$lines.Add("")

# 1) Baseline quick
$v2 = Get-Process v2rayN -EA SilentlyContinue
$xray = Get-Process xray -EA SilentlyContinue
$p10809 = [bool](Get-NetTCPConnection -LocalPort 10809 -State Listen -EA SilentlyContinue)
$p10808 = [bool](Get-NetTCPConnection -LocalPort 10808 -State Listen -EA SilentlyContinue)
$lines.Add("## Baseline")
$lines.Add("- v2rayN: $(if ($v2) { "pid=$($v2.Id)" } else { "DOWN" })")
$lines.Add("- xray: $(if ($xray) { "pid=$($xray.Id)" } else { "DOWN" })")
$lines.Add("- listen 10809=$p10809 10808=$p10808")

# 2) Optimize
$optCode = -1
if (-not $SkipOptimize) {
  Write-Host "Running optimize-cursor-network..."
  & powershell -ExecutionPolicy Bypass -File "E:\dev\CursorTeam\scripts\optimize-cursor-network.ps1"
  $optCode = $LASTEXITCODE
  $lines.Add("")
  $lines.Add("## Optimize")
  $lines.Add("- exit: $optCode (0=stable, 4=agentn fail, 5=partial)")
}

# 3) Expand standard env (priority-2)
$HttpProxy = "http://127.0.0.1:10809"
$SocksProxy = "socks5://127.0.0.1:10808"
$NoProxy = "localhost,127.0.0.1,::1,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,.local"
foreach ($pair in @(
  @{N="HTTP_PROXY";V=$HttpProxy}, @{N="HTTPS_PROXY";V=$HttpProxy},
  @{N="ALL_PROXY";V=$SocksProxy}, @{N="NO_PROXY";V=$NoProxy},
  @{N="http_proxy";V=$HttpProxy}, @{N="https_proxy";V=$HttpProxy},
  @{N="all_proxy";V=$SocksProxy}, @{N="no_proxy";V=$NoProxy}
)) {
  [Environment]::SetEnvironmentVariable($pair.N, $pair.V, "User")
  Set-Item -Path "Env:$($pair.N)" -Value $pair.V -ErrorAction SilentlyContinue
}
git config --global http.proxy $HttpProxy 2>$null
git config --global https.proxy $HttpProxy 2>$null
$lines.Add("")
$lines.Add("## Standard proxy vars")
$lines.Add("- HTTP(S)_PROXY=$HttpProxy")
$lines.Add("- ALL_PROXY=$SocksProxy")
$lines.Add("- git http(s).proxy=$HttpProxy")

# 4) WinHTTP if admin
$winhttpNote = "skipped"
if (-not $SkipWinHttp -and (Is-Admin)) {
  netsh winhttp set proxy proxy-server="127.0.0.1:10809" bypass-list="localhost;127.*;10.*;172.16.*;172.17.*;172.18.*;172.19.*;172.20.*;172.21.*;172.22.*;172.23.*;172.24.*;172.25.*;172.26.*;172.27.*;172.28.*;172.29.*;172.30.*;172.31.*;192.168.*" | Out-Null
  $winhttpNote = "synced 127.0.0.1:10809"
  Write-Host "WinHTTP synced" -ForegroundColor Green
} elseif (-not (Is-Admin)) {
  $winhttpNote = "needs 主控 Admin shell (elevate-cursor-for-main.ps1)"
}
$lines.Add("")
$lines.Add("## WinHTTP")
$lines.Add("- $winhttpNote")

# 5) Preflight
Write-Host "Running preflight..."
$pfArgs = @("-ExecutionPolicy","Bypass","-File","E:\dev\CursorTeam\scripts\task-env-preflight.ps1")
if ($BossConfirmGpt) { $pfArgs += "-BossConfirmGpt" }
& powershell @pfArgs
$pfCode = $LASTEXITCODE
$gate = switch ($pfCode) {
  0 { if ($BossConfirmGpt) { "SOFT-GREEN or GREEN" } else { "GREEN" } }
  4 { "YELLOW — agentn FAIL" }
  3 { "RED — proxy/api2" }
  default { "UNKNOWN $pfCode" }
}
$lines.Add("")
$lines.Add("## Preflight")
$lines.Add("- exit: $pfCode")
$lines.Add("- gate: $gate")
$lines.Add("- BossConfirmGpt: $BossConfirmGpt")

$lines.Add("")
$lines.Add("## Next")
if ($pfCode -eq 0 -and -not $BossConfirmGpt) {
  $lines.Add("- OK: hard green — Task dispatch allowed")
} elseif ($pfCode -eq 0 -and $BossConfirmGpt) {
  $lines.Add("- TEMP: soft green — keep switching v2rayN node until agentn OK")
} else {
  $lines.Add("- ACTION: boss switch v2rayN node; re-run this script until agentn OK")
}

$lines | Set-Content $report -Encoding UTF8
Write-Host "Report: $report"
Write-Host "GATE: $gate"
exit $pfCode
