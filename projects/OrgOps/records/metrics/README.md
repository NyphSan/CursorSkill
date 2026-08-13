# 度量台账

`ledger.csv` 一行一个 cycle 或 session。

| 列 | 含义 |
|----|------|
| duration_s | 墙钟秒 |
| tokens_in / tokens_out | 有环境变量才写数字，否则 `unobserved` |
| tokens_source | `env` 或 `unobserved` |
| skills_promoted | 本周期升格的 name |

禁止把 API 密钥写进本表。
