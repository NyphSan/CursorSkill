#Requires -Version 5.1
param(
  [string]$Name = "scl-pc",
  [string]$WorkerDir = "E:\Project\Game\S_\SCL",
  [switch]$SkipV2ray,
  [switch]$Debug
)
$ErrorActionPreference = "Continue"
if (-not $SkipV2ray -and (Test-Path "E:\dev\CursorTeam\scripts\ensure-v2ray.ps1")) {
  & powershell -ExecutionPolicy Bypass -File "E:\dev\CursorTeam\scripts\ensure-v2ray.ps1"
}
if (-not (Get-Command agent -ErrorAction SilentlyContinue)) {
  Write-Host "Install: irm 'https://cursor.com/install?win32=true' | iex"
  exit 2
}
Set-Location $WorkerDir
git -C $WorkerDir remote -v
$a = @("worker","start","--name",$Name,"--worker-dir",$WorkerDir)
if ($Debug) { $a += "--debug" }
Write-Host "Starting $Name — keep window open. Agents: https://cursor.com/agents"
& agent @a
