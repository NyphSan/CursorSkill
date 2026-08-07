#Requires -Version 5.1
<#
.SYNOPSIS
  Switch v2rayN routing template: Global | Whitelist | Blacklist
  Then restart v2rayN so core regenerates config.json
#>
param(
  [ValidateSet("Global", "Whitelist", "Blacklist")]
  [string]$Mode = "Global",
  [string]$V2rayRoot = "C:\Users\as353\Desktop\VPN\v2rayN-windows-64",
  [switch]$NoRestart,
  [switch]$Netcheck
)

$py = @"
import sqlite3, json, shutil
from pathlib import Path
mode = '$Mode'
root = Path(r'$V2rayRoot')
db = root / 'guiConfigs' / 'guiNDB.db'
gui = root / 'guiConfigs' / 'guiNConfig.json'
c = sqlite3.connect(str(db))
c.row_factory = sqlite3.Row
rows = list(c.execute('SELECT Id, Remarks, IsActive FROM RoutingItem'))
print('before:', [dict(r) for r in rows])
key = {'Global': ('Global', '\u5168\u5c40'), 'Whitelist': ('Whitelist', '\u7ed5\u8fc7'), 'Blacklist': ('Blacklist', '\u9ed1\u540d\u5355')}[mode]
target = None
for r in rows:
    rem = r['Remarks'] or ''
    if any(k in rem for k in key):
        target = r['Id']
        break
if not target:
    raise SystemExit('routing mode not found: ' + mode)
c.execute('UPDATE RoutingItem SET IsActive=0')
c.execute('UPDATE RoutingItem SET IsActive=1 WHERE Id=?', (target,))
c.commit()
g = json.loads(gui.read_text(encoding='utf-8'))
g.setdefault('RoutingBasicItem', {})['RoutingIndexId'] = str(target)
gui.write_text(json.dumps(g, ensure_ascii=False, indent=2), encoding='utf-8')
print('activated', mode, target)
print('after:', [dict(r) for r in c.execute('SELECT Id, Remarks, IsActive FROM RoutingItem')])
c.close()
"@

$tmp = Join-Path $env:TEMP "v2rayn-set-routing.py"
Set-Content -Path $tmp -Value $py -Encoding UTF8
python $tmp
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

if (-not $NoRestart) {
  Write-Host "Restarting v2rayN..."
  Get-Process v2rayN, xray -ErrorAction SilentlyContinue | Stop-Process -Force
  Start-Sleep -Seconds 2
  Start-Process (Join-Path $V2rayRoot "v2rayN.exe") -WorkingDirectory $V2rayRoot
  Start-Sleep -Seconds 5
}

# system proxy — prefer HTTP 10809 (mixed), fallback SOCKS 10808
$ie = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
$proxyHost = if (Get-NetTCPConnection -LocalPort 10809 -State Listen -ErrorAction SilentlyContinue) {
  "127.0.0.1:10809"
} else {
  "127.0.0.1:10808"
}
Set-ItemProperty $ie -Name ProxyEnable -Value 1
Set-ItemProperty $ie -Name ProxyServer -Value $proxyHost
Write-Host "System proxy -> $proxyHost ; Mode=$Mode"

if ($Netcheck) {
  & powershell -ExecutionPolicy Bypass -File "E:\dev\CursorTeam\scripts\cursor-gpt-netcheck.ps1"
}
