---
name: loomle-ue-sal-mcp
description: Use when driving a live Unreal Editor via the Loomle MCP server, especially for Blueprint graphs, UMG widgets, StateTree, or any complex object whose graph is fragile to mutate via raw Python. Loomle introduces SAL (Structured Agent Language) — compact ordered text the agent authors/inspects/edits without going through raw tool calls. Auto-loads any time the user mentions Loomle or asks for agent-friendly UE structure-preserving edits.
---

# Loomle SAL — Unreal Editor MCP with structure-preserving edits

**Loomle** is a local-first MCP bridge for Unreal Engine 5.7 + 5.8 (MIT license). It exposes the live editor through a **three-call SAL interface** instead of one MCP tool per capability:

1. **`sal_schema`** — discover the live object model, with domain guidance and exact editor capabilities
2. **`sal_query`** — read live Unreal state: structure, relationships, execution flow, precise layout geometry
3. **`sal_patch`** — compose ordered edits, dry-run + validate, then apply as one coherent change

Supporting calls handle Client health, explicit project binding, live editor context, presentation control, and **Resident Agent Skills** (loaded through the same MCP connection — no separate host-specific Skill install required).

## Why SAL matters

Text code gives agents precise search, reference, diff and edit. Unreal assets don't. SAL fills that gap:

- **Compact text payloads** — uses far fewer tokens than large generic JSON
- **Query-first summary + local view** — agents don't have to download the whole graph
- **Target-relative stable identity paths** — returned Nodes / Pins / Graphs / Widgets / Blueprints are safe to follow across calls
- **Palette + dynamic schema discovery** — agent reasons about UE's actual exposed capabilities, not a static catalog
- **Dry runs are first-class** — before any mutation the agent shares the real parse / validate / plan path
- **Native compiler + object health diagnostics** — built-in

## Supported Unreal domains

| Module | What's in |
|---|---|
| **Asset** | Asset Registry discovery, asset ops |
| **Blueprint** | Blueprint declaration, components |
| **Class** | Class reflection, defaults |
| **Graph** | Graph-local flow + change |
| **StateTree** | StateTree hierarchy + bindings |
| **Widget / UMG WidgetBlueprint** | Widget tree |
| **Additional**: factual reference queries, compile, save, editor context |

## The bundled `format-unreal-blueprints` skill

Ships **Resident Skill** in the Loomle MCP connection itself: it can acquire authoritative live Graph geometry through Loomle's Editor controls, plan move-only layout changes, validate via dry runs, and verify by readback. With explicit authorization, it can also guide topology improvements like local getters and reroute nodes using exact node-and-pin identities.

## When to pick Loomle vs other UE MCPs

| Aspect | Loomle | ue-mcp | VibeUE |
|---|---|---|---|
| Editor integration | Local MCP Client + native C++ Bridge | C++ Bridge + WebSocket/JSON-RPC | UE 5.8+ native toolset extension |
| Mutation safety | SAL dry-runs first-class | YAML engine + rollback | TransactionService + MCP endpoint |
| Edits representation | Compact SAL text | Generic JSON payloads | Native toolsets + skills |
| Graph mutability | Pin-reconstruction resilient | Native MCP tool calls | Higher-order BP creation |
| Best for | Structure-preserving edits, complex objects | 783+ ops, broad coverage | UE 5.8 toolset extension |

Use Loomle when **graph topology or widget tree identity matters** and you can't afford a malformed edit. Use ue-mcp for the broadest editor surface. Use VibeUE for UE 5.8 native toolset flavor.

## Sharp edges

- Requires a **running Unreal Editor** + MCP-compatible host on the same machine
- Local-only by design (loopback). For remote / LAN use a VPN or auth proxy.
- Currently macOS Apple Silicon + Windows x64 only (darwin-arm64 / win32-x64)
- 8 MCP tools total (`status`, `project`, `sal_query`, `sal_patch`, `sal_schema`, `agent_skill`, `editor`, `python`)

## Search coverage note

- MIT license, repo last updated 2026-08-11 (skill directory adds active commits through 08-09)
- New sighting as of 2026-08-11 — not on 2026-08-10 watch list, fresh addition
