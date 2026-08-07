import sqlite3
from pathlib import Path

db = Path(r"C:\Users\as353\Desktop\VPN\v2rayN-windows-64\guiConfigs\guiNDB.db")
c = sqlite3.connect(str(db))
print("tables:", [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")])
for t in ["ProfileItem", "ProfileExItem", "ProfileGroupItem"]:
    cols = [x[1] for x in c.execute(f"PRAGMA table_info({t})")]
    print(t, cols)
# delays / active hints in ProfileExItem
rows = list(c.execute("SELECT * FROM ProfileExItem LIMIT 1"))
if rows:
    cols = [x[1] for x in c.execute("PRAGMA table_info(ProfileExItem)")]
    print("ProfileExItem sample:", dict(zip(cols, rows[0])))
# count profiles
print("ProfileItem count", c.execute("SELECT count(*) FROM ProfileItem").fetchone()[0])
# top by delay if column exists
cols = [x[1] for x in c.execute("PRAGMA table_info(ProfileItem)")]
excols = [x[1] for x in c.execute("PRAGMA table_info(ProfileExItem)")]
print("excols", excols)
c.close()
