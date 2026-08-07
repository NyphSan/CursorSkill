#Requires -Version 5.1
<#
.SYNOPSIS
  Restart Cursor elevated (UAC). Org rule: only 主控 may use admin Shell.

.NOTES
  After UAC "Yes": reopen the 主控 chat and verify IsAdmin=True.
  Subagents / workers must NOT run this for themselves.
#>
$ErrorActionPreference = 'Stop'

Write-Host "=== elevate-cursor-for-main (主控专用) ===" -ForegroundColor Cyan
Write-Host "规则确认: rules/00_org_charter.md — OS 管理员提权仅主控"
Write-Host ""

$candidates = @(
  (Get-Process -Name 'Cursor' -ErrorAction SilentlyContinue | Select-Object -First 1 -ExpandProperty Path),
  "$env:LOCALAPPDATA\Programs\cursor\Cursor.exe",
  "$env:LOCALAPPDATA\Programs\Cursor\Cursor.exe",
  "$env:ProgramFiles\Cursor\Cursor.exe"
) | Where-Object { $_ -and (Test-Path $_) } | Select-Object -First 1

if (-not $candidates) {
  Write-Host "未找到 Cursor.exe。请改用：右键 Cursor 快捷方式 → 以管理员身份运行" -ForegroundColor Yellow
  exit 2
}

Write-Host "将以管理员重启: $candidates"
Write-Host "请在 UAC 对话框点「是」。然后重新打开本主控对话。"
Start-Process -FilePath $candidates -Verb RunAs
exit 0
