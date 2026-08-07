#Requires -Version 5.1
<#
.SYNOPSIS
  Preflight before any Task / Cloud worker job.
  Exit 0 = Task OK to dispatch; 4 = agentn fail (no Task); 3 = proxy down.
#>
param(
  [switch]$OptimizeFirst,
  [switch]$AllowLocalOnly,
  # Boss confirmed GPT works in Cursor UI (agentn curl may still false-fail)
  [switch]$BossConfirmGpt
)

$ErrorActionPreference = "Continue"
Write-Host "=== task-env-preflight ===" -ForegroundColor Cyan

if ($OptimizeFirst) {
  $opt = "E:\dev\CursorTeam\scripts\optimize-cursor-network.ps1"
  if (Test-Path $opt) {
    & powershell -ExecutionPolicy Bypass -File $opt
  }
}

$check = "E:\dev\CursorTeam\scripts\cursor-gpt-netcheck.ps1"
& powershell -ExecutionPolicy Bypass -File $check
$code = $LASTEXITCODE

$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$dir = "E:\dev\CursorTeam\docs\network"
New-Item -ItemType Directory -Force -Path $dir | Out-Null
$report = Join-Path $dir ("PREFLIGHT-{0}.md" -f $stamp)

$status = switch ($code) {
  0 { "GREEN — Task/GPT Agent OK" }
  4 { "YELLOW — api2 OK, agentn FAIL — DO NOT dispatch Task" }
  3 { "RED — proxy/api2 down" }
  default { "UNKNOWN exit=$code" }
}

@"
# PREFLIGHT $stamp

- **status:** $status
- **exit:** $code
- **rule:** rules/08_network_ops.md — every Task must pass preflight

## Gate
| Check | Meaning |
|-------|---------|
| exit 0 | Dispatch Task OK |
| exit 4 | Switch v2ray node; main may local-only if AllowLocalOnly |
| exit 3 | Run ensure-v2ray / optimize first |
"@ | Set-Content $report -Encoding UTF8

Write-Host "Report: $report"
Write-Host "STATUS: $status"

if ($code -eq 0) { exit 0 }

# Soft green: api2 OK (exit 4 from netcheck) + boss confirms GPT in UI
if ($code -eq 4 -and $BossConfirmGpt) {
  Write-Host "SOFT-GREEN: BossConfirmGpt — allow Task; agentn curl still FAIL (monitor TLS)" -ForegroundColor Yellow
  @"

## Boss override
- BossConfirmGpt=true (manual GPT OK in Cursor UI)
- agentn curl still failed — Task may still TLS-abort; prefer Global + same node that works for GPT
"@ | Add-Content $report -Encoding UTF8
  exit 0
}

if ($code -eq 4 -and $AllowLocalOnly) {
  Write-Host "AllowLocalOnly: main session may proceed WITHOUT Task" -ForegroundColor Yellow
  exit 4
}
exit $code
