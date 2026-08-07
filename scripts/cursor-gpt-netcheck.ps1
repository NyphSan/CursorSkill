#Requires -Version 5.1
param(
  [string]$SocksProxy = "socks5h://127.0.0.1:10808",
  [string]$HttpProxy = "http://127.0.0.1:10809"
)

$ErrorActionPreference = "Continue"
Write-Host "=== Cursor GPT / Agent network check ===" -ForegroundColor Cyan

function Test-Url {
  param([string]$Url, [string]$Proxy, [string]$Label)
  Write-Host "[$Label] $Url"
  $out = & curl.exe -sS -o NUL -w "code=%{http_code} time=%{time_total}" --proxy $Proxy --connect-timeout 12 --max-time 20 $Url 2>&1
  $text = ($out | Out-String).Trim()
  if ($text -match "HTTP/0\.9") {
    Write-Host "  FAIL  HTTP/0.9 (bad node/link for Agent)" -ForegroundColor Red
    return $false
  }
  if ($text -match "code=000" -or $text -match "timed out" -or $text -match "Failed to connect") {
    Write-Host "  FAIL  $text" -ForegroundColor Red
    return $false
  }
  if ($text -match "code=(200|401|403|404)") {
    Write-Host "  OK    $text" -ForegroundColor Green
    return $true
  }
  Write-Host "  WARN  $text" -ForegroundColor Yellow
  return $false
}

try {
  $ie = Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
  Write-Host ("SystemProxy Enable={0} Server={1}" -f $ie.ProxyEnable, $ie.ProxyServer)
} catch {}

foreach ($port in @(10808, 10809)) {
  $listen = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
  if ($listen) {
    $proc = Get-Process -Id ($listen.OwningProcess | Select-Object -First 1) -ErrorAction SilentlyContinue
    Write-Host ("LISTEN {0}  {1}" -f $port, $proc.ProcessName)
  } else {
    Write-Host ("NO LISTEN {0}" -f $port)
  }
}
Write-Host ""

$httpUp = [bool](Get-NetTCPConnection -LocalPort 10809 -State Listen -ErrorAction SilentlyContinue)
$primary = if ($httpUp) { $HttpProxy } else { $SocksProxy }
$tag = if ($httpUp) { "HTTP" } else { "SOCKS" }

$agentOk = Test-Url "https://agentn.global.api5.cursor.sh/" $primary "$tag-agentn"
$api2Ok  = Test-Url "https://api2.cursor.sh/" $primary "$tag-api2"
$oaiOk   = Test-Url "https://api.openai.com/v1/models" $primary "$tag-openai"
$null = Test-Url "https://api2direct.cursor.sh/" $primary "$tag-api2direct"

Write-Host ""
Write-Host "=== Verdict ===" -ForegroundColor Cyan
if ($agentOk -and $api2Ok) {
  Write-Host "STABLE: Agent endpoint OK. Restart Cursor if needed, then use GPT/Task." -ForegroundColor Green
  exit 0
} elseif ($api2Ok -and -not $agentOk) {
  Write-Host "UNSTABLE: api2 OK but agentn FAIL -> switch v2rayN NODE (Global alone is not enough)." -ForegroundColor Yellow
  exit 4
} else {
  Write-Host "DOWN: api2 FAIL -> fix v2rayN first." -ForegroundColor Red
  exit 3
}
