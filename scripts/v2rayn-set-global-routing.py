import sqlite3, json, shutil
from pathlib import Path

db = Path(r"C:\Users\as353\Desktop\VPN\v2rayN-windows-64\guiConfigs\guiNDB.db")
gui = Path(r"C:\Users\as353\Desktop\VPN\v2rayN-windows-64\guiConfigs\guiNConfig.json")
bak = db.with_suffix(".db.bak-before-global")
if not bak.exists():
    shutil.copy2(db, bak)
    print("backup:", bak)

c = sqlite3.connect(str(db))
c.row_factory = sqlite3.Row
rows = list(c.execute("SELECT Id, Remarks, IsActive FROM RoutingItem"))
print("before:")
for r in rows:
    print(dict(r))

GLOBAL_ID = None
for r in rows:
    rem = r["Remarks"] or ""
    if "Global" in rem or "\u5168\u5c40" in rem:
        GLOBAL_ID = r["Id"]

if not GLOBAL_ID:
    raise SystemExit("Global routing not found")

c.execute("UPDATE RoutingItem SET IsActive=0")
c.execute("UPDATE RoutingItem SET IsActive=1 WHERE Id=?", (GLOBAL_ID,))
c.commit()
print("activated Global Id=", GLOBAL_ID)

print("after:")
for r in c.execute("SELECT Id, Remarks, IsActive FROM RoutingItem"):
    print(dict(r))

g = json.loads(gui.read_text(encoding="utf-8"))
g.setdefault("RoutingBasicItem", {})["RoutingIndexId"] = str(GLOBAL_ID)
gui.write_text(json.dumps(g, ensure_ascii=False, indent=2), encoding="utf-8")
print("guiNConfig RoutingIndexId ->", GLOBAL_ID)

rule = c.execute("SELECT RuleSet FROM RoutingItem WHERE Id=?", (GLOBAL_ID,)).fetchone()[0]
rules = json.loads(rule)
print("Global rules count:", len(rules))
for x in rules:
    print("-", x.get("Remarks"), "->", x.get("OutboundTag"))
c.close()
print("DONE")
