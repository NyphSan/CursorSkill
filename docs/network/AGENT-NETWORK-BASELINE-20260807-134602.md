# AGENT NETWORK BASELINE 20260807-134602

## Phase 1 — NETWORK_BASELINE (read-only)

### System
- Windows: Microsoft Windows 11 专业版 (Build 22631)
- PowerShell: 5.1.22621.6133
- User: NYPH\as353
- Admin: False
- Arch: AMD64
- Time: 2026-08-07 13:46:03
- TZ: China Standard Time

### Adapters (active IPv4)
- Radmin VPN | IPv4=26.5.20.168 | GW=26.0.0.1 | DNS=fec0:0:0:ffff::1, fec0:0:0:ffff::2, fec0:0:0:ffff::3 | DHCP=Disabled | Metric=1
- 以太网 | IPv4=192.168.3.21 | GW=192.168.3.1 | DNS=223.5.5.5, 180.76.76.76 | DHCP=Enabled | Metric=25
- VMware Network Adapter VMnet1 | IPv4=192.168.23.1 | GW=- | DNS=fec0:0:0:ffff::1, fec0:0:0:ffff::2, fec0:0:0:ffff::3 | DHCP=Enabled | Metric=35
- VMware Network Adapter VMnet8 | IPv4=192.168.124.1 | GW=- | DNS=fec0:0:0:ffff::1, fec0:0:0:ffff::2, fec0:0:0:ffff::3 | DHCP=Enabled | Metric=35
- WLAN | IPv4=169.254.194.245 | GW=- | DNS=172.20.10.1 | DHCP=Enabled | Metric=25
- 蓝牙网络连接 | IPv4=169.254.213.72 | GW=- | DNS=- | DHCP=Enabled | Metric=65

### Default route (top)
    ===========================================================================
    接口列表
     12...02 50 18 b7 2f 1e ......Famatech Radmin VPN Ethernet Adapter
     20...a8 a1 59 b5 6d 7c ......Intel(R) Ethernet Connection (17) I219-V
     13...d4 54 8b 5e 1c 9e ......Intel(R) Wi-Fi 6 AX200 160MHz
      6...d4 54 8b 5e 1c 9f ......Microsoft Wi-Fi Direct Virtual Adapter
      5...d6 54 8b 5e 1c 9e ......Microsoft Wi-Fi Direct Virtual Adapter #2
     21...00 50 56 c0 00 01 ......VMware Virtual Ethernet Adapter for VMnet1
      7...00 50 56 c0 00 08 ......VMware Virtual Ethernet Adapter for VMnet8
     22...d4 54 8b 5e 1c a2 ......Bluetooth Device (Personal Area Network)
      1...........................Software Loopback Interface 1
    ===========================================================================
    
    IPv4 路由表
    ===========================================================================
    活动路由:
    网络目标        网络掩码          网关       接口   跃点数
              0.0.0.0          0.0.0.0         26.0.0.1      26.5.20.168   9257
              0.0.0.0          0.0.0.0      192.168.3.1     192.168.3.21     25
             26.0.0.0        255.0.0.0            在链路上       26.5.20.168    257
          26.5.20.168  255.255.255.255            在链路上       26.5.20.168    257
       26.255.255.255  255.255.255.255            在链路上       26.5.20.168    257
            127.0.0.0        255.0.0.0            在链路上         127.0.0.1    331
            127.0.0.1  255.255.255.255            在链路上         127.0.0.1    331
      127.255.255.255  255.255.255.255            在链路上         127.0.0.1    331
          192.168.3.0    255.255.255.0            在链路上      192.168.3.21    281
         192.168.3.21  255.255.255.255            在链路上      192.168.3.21    281
        192.168.3.255  255.255.255.255            在链路上      192.168.3.21    281
         192.168.23.0    255.255.255.0            在链路上      192.168.23.1    291
         192.168.23.1  255.255.255.255            在链路上      192.168.23.1    291
       192.168.23.255  255.255.255.255            在链路上      192.168.23.1    291
        192.168.124.0    255.255.255.0            在链路上     192.168.124.1    291
        192.168.124.1  255.255.255.255            在链路上     192.168.124.1    291
      192.168.124.255  255.255.255.255            在链路上     192.168.124.1    291
            224.0.0.0        240.0.0.0            在链路上         127.0.0.1    331
            224.0.0.0        240.0.0.0            在链路上       26.5.20.168    257
            224.0.0.0        240.0.0.0            在链路上      192.168.23.1    291
            224.0.0.0        240.0.0.0            在链路上     192.168.124.1    291
            224.0.0.0        240.0.0.0            在链路上      192.168.3.21    281
      255.255.255.255  255.255.255.255            在链路上         127.0.0.1    331
      255.255.255.255  255.255.255.255            在链路上       26.5.20.168    257
      255.255.255.255  255.255.255.255            在链路上      192.168.23.1    291
      255.255.255.255  255.255.255.255            在链路上     192.168.124.1    291
      255.255.255.255  255.255.255.255            在链路上      192.168.3.21    281
    ===========================================================================
    永久路由:
      网络地址          网络掩码  网关地址  跃点数
              0.0.0.0          0.0.0.0         26.0.0.1    9256
    ===========================================================================

## Phase 2 — Proxy / DNS / TUN
- WinIE ProxyEnable=1 ProxyServer=127.0.0.1:10809 ProxyOverride=localhost;127.*;10.*;172.16.*;172.17.*;172.18.*;172.19.*;172.20.*;172.21.*;172.22.*;172.23.*;172.24.*;172.25.*;172.26.*;172.27.*;172.28.*;172.29.*;172.30.*;172.31.*;192.168.*
- WinHTTP:
    当前的 WinHTTP 代理服务器设置:
        直接访问(没有代理服务器)。
- Env vars (process):
  - HTTP_PROXY: Process=http://127.0.0.1:10809 | User=http://127.0.0.1:10809 | Machine=
  - HTTPS_PROXY: Process=http://127.0.0.1:10809 | User=http://127.0.0.1:10809 | Machine=
  - NO_PROXY: Process=localhost,127.0.0.1 | User=localhost,127.0.0.1 | Machine=
  - http_proxy: Process=http://127.0.0.1:10809 | User=http://127.0.0.1:10809 | Machine=
  - https_proxy: Process=http://127.0.0.1:10809 | User=http://127.0.0.1:10809 | Machine=
  - no_proxy: Process=localhost,127.0.0.1 | User=localhost,127.0.0.1 | Machine=

### Focus listen ports
- port 7890: not listening
- port 7891: not listening
- port 7897: not listening
- port 1080: not listening
- port 10808 Local=127.0.0.1 PID=30860 Proc=xray
- port 10809 Local=127.0.0.1 PID=30860 Proc=xray
- port 3128: not listening
- port 8080 Local=127.0.0.1 PID=19000 Proc=steamwebhelper

### 127.0.0.1 listeners (sample)
- :::80 PID=24932 gitea-1.22.3-windows-4.0-386
- :::135 PID=1468 svchost
- :::445 PID=4 System
- 0.0.0.0:902 PID=3364 vmware-authd
- 0.0.0.0:912 PID=3364 vmware-authd
- ::1:1025 PID=5628 jhi_service
- :::1037 PID=1148 services
- 127.0.0.1:1041 PID=5836 AweSun
- 127.0.0.1:1042 PID=5836 AweSun
- 127.0.0.1:3778 PID=26496 node
- 127.0.0.1:3779 PID=26496 node
- 127.0.0.1:4001 PID=2716 QQ
- 127.0.0.1:4301 PID=2716 QQ
- 127.0.0.1:4310 PID=2716 QQ
- 127.0.0.1:4701 PID=4916 yEd
- 127.0.0.1:4709 PID=25388 wpscloudsvr
- 127.0.0.1:4875 PID=18892 steam
- 127.0.0.1:4877 PID=18892 steam
- :::5021 PID=25388 wpscloudsvr
- 0.0.0.0:5040 PID=7512 svchost
- 127.0.0.1:5283 PID=2716 QQ
- 127.0.0.1:5768 PID=26496 node
- :::7680 PID=16108 svchost
- 127.0.0.1:8080 PID=19000 steamwebhelper
- 0.0.0.0:8082 PID=2716 QQ
- 127.0.0.1:9001 PID=18308 frpc
- 127.0.0.1:9210 PID=2716 QQ
- 127.0.0.1:10000 PID=9188 YunDetectService
- 127.0.0.1:10808 PID=30860 xray
- 127.0.0.1:10809 PID=30860 xray
- ::1:18789 PID=13988 node
- 127.0.0.1:18791 PID=13988 node
- 127.0.0.1:18792 PID=13988 node
- 0.0.0.0:27036 PID=18892 steam
- 127.0.0.1:27060 PID=18892 steam
- 127.0.0.1:35600 PID=3140 ToDesk
- ::1:35783 PID=16536 EpicOnlineServicesUserHelper
- 127.0.0.1:35800 PID=3140 ToDesk
- 127.0.0.1:37600 PID=15540 ToDesk
- 127.0.0.1:45623 PID=26496 node
- :::49664 PID=1180 lsass
- 0.0.0.0:49665 PID=1068 wininit
- :::49666 PID=2688 svchost
- 0.0.0.0:49667 PID=3596 svchost
- 0.0.0.0:49669 PID=4236 spoolsv
- 127.0.0.1:58927 PID=25644 HipsDaemon

### Proxy / VPN processes
- FOUND process: v2rayN pid=11248
- FOUND process: xray pid=30860

### TUN / virtual adapters
TUN_EXIST
- Radmin VPN | Status=Up | Desc=Famatech Radmin VPN Ethernet Adapter | IPv4=26.5.20.168


## Phase 2b — listen / process / TUN (refresh)
- port 7890: not listening
- port 7891: not listening
- port 7897: not listening
- port 1080: not listening
- port 10808 Local=127.0.0.1 PID=30860 Proc=xray
- port 10809 Local=127.0.0.1 PID=30860 Proc=xray
- port 3128: not listening
- port 8080 Local=127.0.0.1 PID=19000 Proc=steamwebhelper

### Proxy/VPN processes
- FOUND: v2rayN pid=11248
- FOUND: xray pid=30860

### TUN adapters
TUN_EXIST (virtual/VPN adapters present; evaluate if system-wide TUN)
- Radmin VPN | Status=Up | Desc=Famatech Radmin VPN Ethernet Adapter | IPv4=26.5.20.168 | Metric=

### Proxy connect probe
- HTTP 127.0.0.1:10809 TcpOpen=True
- SOCKS 127.0.0.1:10808 TcpOpen=True
- HTTP 127.0.0.1:7890 TcpOpen=False

## Phase 3 — Agent ecosystem
- git: git version 2.47.0.windows.1
- git http.proxy: http://127.0.0.1:10808
- git https.proxy: http://127.0.0.1:10808
- git http.sslVerify: (default)
- node: v24.11.1
- npm: 11.6.2
- npm registry: https://registry.npmjs.org/
- npm proxy: null
- npm https-proxy: null
- pnpm: 10.33.0
- yarn: node.exe : ! Corepack is about to download https://registry.yarnpkg.com/yarn/-/yarn-1.22.22.tgz
所在位置 C:\Program Files\nodejs\yarn.ps1:16 字符: 5
+     & "$basedir/node$exe"  "$basedir/node_modules/corepack/dist/yarn. ...
+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (! Corepack is a...arn-1.22.22.tgz:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
1.22.22
- python: Python 3.14.5
- pip: pip 26.1.1 from C:\Users\as353\AppData\Local\Programs\Python\Python314\Lib\site-packages\pip (python 3.14)
- pip proxy: ERROR: No such key - global.proxy
- docker: NOT_INSTALLED
- agent(cursor): 2026.08.04-aaa8809
- AI CLI codex: NOT_FOUND
- AI CLI claude: NOT_FOUND
- AI CLI gemini: FOUND
- AI CLI gh: NOT_FOUND
- AI CLI aider: NOT_FOUND
- AI CLI opencode: NOT_FOUND
- AI CLI cursor-agent: FOUND
- ssh config: NOT_FOUND

### Credential presence (no secrets)
FOUND_CREDENTIAL source=C:\Users\as353\.codex\auth.json
FOUND_CREDENTIAL source=C:\Users\as353\.cursor\argv.json

## Phase 4 — Capability tests
- HTTPS https://github.com: PASS HTTPS status=200
- HTTPS https://api.openai.com/v1/models: PASS HTTPS AUTH_BOUNDARY status=401 (network OK)
- HTTPS https://api.anthropic.com: APPLICATION_FAILURE status=404
- HTTPS https://registry.npmjs.org/: PASS HTTPS status=200
- HTTPS https://pypi.org: PASS HTTPS status=200
- HTTPS https://huggingface.co: PASS HTTPS status=200
- HTTPS https://api2.cursor.sh: PASS HTTPS status=200

### Git ls-remote
- git: 2c78326f810173a4f3aefd8021f1e07575412481	HEAD

### npm ping
- npm: node.exe : npm notice PING https://registry.npmjs.org/
所在位置 行:1 字符: 1
+ & "C:\Program Files\nodejs/node.exe" "C:\Program Files\nodejs/node_mo ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (npm notice PING...stry.npmjs.org/:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
npm notice PONG 2943ms

### pip index
- pip: pip : WARNING: Cache entry deserialization failed, entry ignored
所在位置 C:\Users\as353\AppData\Local\Temp\ps-script-e77fec8a-d43d-4b31-a543-506de21a2f38.ps1:302 字符: 20
+   $pipOut = Safe { pip index versions pip 2>&1 | Select-Object -First ...
+                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (WARNING: Cache ..., entry ignored:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
pip (26.2.1)
Available versions: 26.2.1, 26.2, 26.1.2, 26.1.1, 26.1, 26.0.1, 26.0, 25.3, 25.2, 25.1.1, 25.1, 25.0.1, 25.0, 24.3.1, 24.3, 24.2, 24.1.2, 24.1.1, 24.1, 24.0, 23.3.2, 23.3.1, 23.3, 23.2.1, 23.2, 23.1.2, 23.1.1, 23.1, 23.0.1, 23.0, 22.3.1, 22.3, 22.2.2, 22.2.1, 22.2, 22.1.2, 22.1.1, 22.1, 22.0.4, 22.0.3, 22.0.2, 22.0.1, 22.0, 21.3.1, 21.3, 21.2.4, 21.2.3, 21.2.2, 21.2.1, 21.1.3, 21.1.2, 21.1.1, 21.1, 21.0.1, 21.0, 20.3.4, 20.3.3, 20.3.1, 20.3, 20.2.4, 20.2.3, 20.2.2, 20.2.1, 20.2, 20.1.1, 20.1, 20.0.2, 20.0.1, 19.3.1, 19.3, 19.2.3, 19.2.2, 19.2.1, 19.2, 19.1.1, 19.1, 19.0.3, 19.0.2, 19.0.1, 19.0, 18.1, 18.0, 10.0.1, 10.0.0, 9.0.3, 9.0.2, 9.0.1, 9.0.0, 8.1.2, 8.1.1, 8.1.0, 8.0.3, 8.0.2, 8.0.1, 8.0.0, 7.1.2, 7.1.1, 7.1.0, 7.0.3, 7.0.2, 7.0.1, 7.0.0, 6.1.1, 6.1.0, 6.0.8, 6.0.7, 6.0.6, 6.0.5, 6.0.4, 6.0.3, 6.0.2, 6.0.1, 6.0, 1.5.6, 1.5.5, 1.5.4, 1.5.3, 1.5.2, 1.5.1, 1.5, 1.4.1, 1.4, 1.3.1, 1.3, 1.2.1, 1.2, 1.1, 1.0.2, 1.0.1, 1.0, 0.8.3, 0.8.2, 0.8.1, 0.8, 0.7.2, 0.7.1, 0.7, 0.6.3, 0.6.2, 0.6.1, 0.6, 0.5.1, 0.5, 0.4, 0.3.1, 0.3, 0.2.1, 0.2
  INSTALLED: 26.1.1
  LATEST:    26.2.1

### docker
- docker: SKIP NOT_INSTALLED

