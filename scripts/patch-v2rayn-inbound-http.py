import json
from pathlib import Path

p = Path(r"C:\Users\as353\Desktop\VPN\v2rayN-windows-64\guiConfigs\guiNConfig.json")
g = json.loads(p.read_text(encoding="utf-8"))
inbound = g["Inbound"][0]
inbound["Protocol"] = "mixed"
inbound["SecondLocalPortEnabled"] = True
inbound["LocalPort"] = 10808
inbound["UdpEnabled"] = True
inbound["SniffingEnabled"] = True
# Prefer system proxy stability; TUN needs admin — keep current Tun flag
p.write_text(json.dumps(g, ensure_ascii=False, indent=2), encoding="utf-8")
print("OK protocol=", inbound["Protocol"], "SecondLocalPort=", inbound["SecondLocalPortEnabled"])
print("EnableTun=", g.get("TunModeItem", {}).get("EnableTun"))
