#Requires -Version 5.1
<#
.SYNOPSIS
  Start Cursor My Machines worker for CursorTeam (ORG_ROOT).
  Keep this window open. Cloud Agent tool calls land on this PC.
#>
param(
  [string]$Name = "cursorteam-pc",
  [string]$WorkerDir = "E:\dev\CursorTeam",
  [switch]$SkipV2ray,
  [switch]$Debug
)

$ErrorActionPreference = "Continue"
Write-Host "=== start-org-worker ===" -ForegroundColor Cyan
Write-Host "name=$Name dir=$WorkerDir"

if (-not $SkipV2ray) {
  $ensure = "E:\dev\CursorTeam\scripts\ensure-v2ray.ps1"
  if (Test-Path $ensure) {
    Write-Host "Ensuring v2ray..."
    & powershell -ExecutionPolicy Bypass -File $ensure
  }
}

if (-not (Get-Command agent -ErrorAction SilentlyContinue)) {
  Write-Host "agent CLI not found. Install:" -ForegroundColor Yellow
  Write-Host "  irm 'https://cursor.com/install?win32=true' | iex"
  exit 2
}

if (-not (Test-Path $WorkerDir)) {
  Write-Host "WorkerDir missing: $WorkerDir" -ForegroundColor Red
  exit 3
}

Set-Location $WorkerDir
Write-Host "git remote:"
git -C $WorkerDir remote -v

Write-Host ""
Write-Host "Starting worker (keep this process running)..." -ForegroundColor Green
Write-Host "Then open https://cursor.com/agents and select env: $Name"
Write-Host "Slack: @Cursor worker=$Name ..."

$args = @("worker", "start", "--name", $Name, "--worker-dir", $WorkerDir)
if ($Debug) { $args = @("worker", "start", "--name", $Name, "--worker-dir", $WorkerDir, "--debug") }

& agent @args
exit $LASTEXITCODE
