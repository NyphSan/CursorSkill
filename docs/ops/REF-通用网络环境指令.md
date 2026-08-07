配置通用网络环境指令
你现在负责初始化当前 Windows 开发机的 AI Agent 通用网络环境。目标不是只支持 Codex，而是建立一个能够兼容市面主流 AI Agent、CLI开发工具、代码助手和AI开发框架的稳定网络基础环境，包括但不限于：OpenAI Codex、ChatGPT CLI、Claude Code、Gemini CLI、Cursor Agent、Continue、Cline、Roo Code、Aider、OpenCode、GitHub Copilot CLI以及基于Node/Python的AI SDK环境。
你的执行原则：
不要假设任何已有网络配置。
不要复制其他机器参数。
不要直接套用固定代理端口。
必须先获取当前机器真实网络状态，再根据检测结果自主选择最佳网络架构。
目标是建立稳定、通用、低维护、长期可用的Agent开发网络环境。
所有修改必须遵循：
检测 → 分析 → 备份 → 修改 → 测试 → 保留或回滚。
如果当前环境已经满足要求，不要继续修改。
==============================
第一阶段：建立完整网络基线 NETWORK_BASELINE
==============================
首先只读采集当前机器环境。
禁止修改任何配置。
采集：
系统：
Windows版本
PowerShell版本
当前用户
管理员权限状态
系统架构
当前时间
时区
网络接口：
所有网络适配器
当前活动接口
IPv4
IPv6
MAC地址
DHCP状态
默认网关
DNS服务器
接口Metric
实际出口网络
路由：
route print
默认路由
Metric
VPN路由
TUN相关路由
==============================
第二阶段：检测代理、DNS、TUN真实环境
==============================
检测所有可能影响Agent联网的配置。
代理：
检查：
Windows系统代理
WinHTTP Proxy
环境变量：
HTTP_PROXY
HTTPS_PROXY
ALL_PROXY
NO_PROXY
同时检查：
http_proxy
https_proxy
all_proxy
no_proxy
记录：
是否存在代理
代理协议
地址
端口
来源
不要假设：
127.0.0.1:7890
或者任何固定端口。
必须通过实际监听和连接测试确认。
扫描本机监听：
重点：
7890
7891
7897
1080
10808
10809
3128
8080
以及所有127.0.0.1监听端口。
记录：
端口
PID
进程
协议类型
检测：
Clash
Clash Verge
Mihomo
sing-box
v2rayN
WARP
VPN客户端
TUN驱动
检测：
Wintun
WireGuard
TAP
虚拟网卡
输出：
TUN_EXIST
或者：
TUN_NOT_FOUND
如果存在：
记录：
接口名称
IP
状态
路由规则
==============================
第三阶段：检测Agent开发生态兼容性
==============================
检查当前机器是否能够支持主流Agent工具。
检查：
Git：
git config --global --list
确认：
http.proxy
https.proxy
Node：
node版本
npm版本
npm registry
npm proxy
pnpm：
pnpm版本
pnpm proxy
yarn：
yarn proxy
Python：
python版本
pip版本
pip proxy
Docker：
docker版本
registry访问状态
SSH：
~/.ssh/config
检查AI工具：
Codex
Claude Code
Gemini CLI
Cursor相关CLI
Continue
Cline
Roo Code
Aider
OpenCode
GitHub Copilot CLI
如果存在：
检测：
安装位置
运行状态
网络继承情况
禁止输出：
Token
API Key
密码
Cookie
代理订阅链接
认证信息
如果发现敏感信息：
只输出：
FOUND_CREDENTIAL
以及来源位置。
==============================
第四阶段：网络能力测试
==============================
执行完整测试：
DNS：
github.com
api.openai.com
api.anthropic.com
generativelanguage.googleapis.com
registry.npmjs.org
pypi.org
huggingface.co
HTTPS：
测试TLS握手。
测试HTTPS访问。
Git：
git ls-remote https://github.com/git/git
Node：
npm访问registry。
Python：
pip访问PyPI。
Docker：
测试registry连接。
区分：
DNS_FAILURE
TCP_FAILURE
TLS_FAILURE
PROXY_FAILURE
AUTH_FAILURE
APPLICATION_FAILURE
不要把：
401
403
权限限制
误判为网络失败。
==============================
第五阶段：自主构建Agent通用网络方案
==============================
根据检测结果选择方案。
优先级：
第一优先：
如果存在稳定TUN模式。
保持TUN作为系统级网络层。
不要重复设置大量软件代理。
第二优先：
如果存在稳定HTTP/SOCKS代理。
确认协议。
确认端口。
配置标准代理变量。
第三优先：
如果系统代理无法覆盖CLI工具。
补充：
HTTP_PROXY
HTTPS_PROXY
ALL_PROXY
NO_PROXY
第四优先：
只针对特殊工具配置：
Git
npm
pip
Docker
AI CLI工具
目标：
让大部分Agent无需单独配置即可工作。
==============================
第六阶段：自动修复规则
==============================
所有修改：
必须先备份。
执行：
BACKUP
CHANGE
TEST
失败：
ROLLBACK
一次只修改一个层级。
禁止：
关闭SSL验证
设置http.sslVerify=false
关闭防火墙
安装未知证书
修改系统路由
删除已有代理软件
删除VPN组件
执行network reset
执行winsock reset
除非经过明确授权。
==============================
第七阶段：最终验收
==============================
完成后：
关闭当前终端。
重新打开新的PowerShell。
确认配置真实继承。
必须测试：
[PASS] DNS
[PASS] HTTPS
[PASS] GitHub
[PASS] Git
[PASS] npm
[PASS] pnpm
[PASS] pip
[PASS] Docker
[PASS] OpenAI服务
[PASS] Anthropic服务
[PASS] Gemini服务
[PASS] HuggingFace
[PASS] Codex
[PASS] Claude Code
[PASS] Gemini CLI
[PASS] 其他Agent CLI环境
最终输出：
AGENT_NETWORK_CONFIGURATION_COMPLETE
报告：
当前网络架构
当前代理方案
实际代理地址和端口
DNS方案
TUN状态
环境变量状态
Git配置
Node生态配置
Python生态配置
Docker状态
Agent兼容性测试结果
修改内容
保留内容
回滚方法
你拥有执行普通诊断命令和低风险配置调整的自主权限。
不需要每一步询问。
只有以下情况必须停止：
需要管理员权限进行重大系统修改
需要安装新网络软件
需要导入证书
需要修改防火墙
需要修改系统路由
需要获取账号凭证
可能破坏现有网络环境
现在开始：
执行 NETWORK_BASELINE，然后自主完成配置和验证。
