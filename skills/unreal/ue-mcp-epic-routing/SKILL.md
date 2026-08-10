---
name: ue-mcp-epic-routing
description: Use when deciding whether to call a ue-mcp native action or route through Epic's Toolset Registry `epic_*` actions. Covers the availability check, when native wins (idempotency, rollback, structured transactions), when epic wins (graph DSL, newer 5.8 features), and how to gracefully fall back. Auto-loads on any ue-mcp call when UE 5.8+ Toolset plugins may be enabled.
---

# ue-mcp epic-routing — pick the right path

ue-mcp exposes **two parallel routes** into the editor for many operations:

- **Native handlers** — C++ handlers we own, in the bridge plugin. Stable, idempotency-aware, transaction-aware.
- **`epic_*` actions** — surfaces operations from Epic's official Toolset Registry. Newer, sometimes richer, but no built-in rollback / transactions.

Choose deliberately. The wrong choice can mean missing validations, or hitting editor features the agent doesn't yet know about.

## Before every operation: check availability

```text
epic(action="status")
```

If `status` returns "available" and reports the toolset supports your operation, **prefer `epic_*` for graph / blueprint body authoring** and **stick with native for everything else**.

## Decision matrix

| Operation domain | Native (`ue-mcp`) | Epic (`epic_*`) | Choose |
|---|---|---|---|
| Blueprint graph **body** (event graph, function body, macro body) | `blueprint(action="add_node"|"connect_pins"|...)` — node-by-node | `epic(action="write_graph_dsl", ...)` — S-expression, one round-trip + compile | **Epic** when available (one pass, no node drift) |
| Blueprint **declaration** (parent class, variables, components, CDO) | `blueprint(action="read"|"set_variable"|"add_component"|...)` | Limited or none | **Native** |
| Blueprint **compilation + validation** | `blueprint(action="compile"|"validate")` | Routes through editor's own compile | **Native** (transactional + status field) |
| Blueprint **interfaces / event dispatchers** | Native | None | **Native** |
| Asset search / read | `asset(action="list"|"search"|"read")` | Limited | **Native** |
| Level / actor mutations | `level(action="...")` | Limited | **Native** |
| Niagara emitter edits | `niagara(action="...")` | `epic(action="...")` may exist for 5.8 | Prefer whichever has the specific op; check `epic(action="status")` first |
| Material graph authoring | `material(action="...")` | Rare | **Native** |
| C++ class generation / native bridge extension | `cpp(action="...")` | None | **Native only** |
| Project settings, plugins, packaging | `project(action="...")` | None | **Native** |
| Editor lifecycle (start/stop/restart) | `editor(action="...")` | None | **Native** |

## Why Epic wins for graph bodies

Node-by-node `add_node` + `connect_pins` produces multiple failed iterations as you discover correct pin names, default values, and connection type compatibility. Epic's graph DSL (S-expression):

- Authors **and compiles** the whole graph in a single round-trip
- Reads doc-style examples via `epic(action="get_graph_dsl_docs")` so the agent has the grammar
- Pin reconstruction is handled by the engine, not by your sequence of calls

For node counts above ~5, prefer Epic's DSL. Below that, both work — pick by familiarity.

## Why native still wins most of the time

- **Transactions**: native handlers wrap mutations in editor `ScopedTransaction`. The user gets Undo support for free. Epic toolset ops don't.
- **Idempotency**: native handlers can declare safe-to-retry semantics. Epic can't.
- **Read-then-mutate discipline**: native has explicit `read` actions to surface current state. Epic relies on the editor's intrinsic "current state" reads.
- **Status fields**: native returns `dirty_packages`, `compile_warnings`, etc. Epic often returns only "ok / not ok".
- **MCP client scope**: native is owned by the bridge plugin; Epic toolset registry is engine-wide. Mixing them widens the trust surface.

## Fallback pattern

When `epic(action="status")` says "not available" (pre-5.8, or the registry is off), fall back to native — never fail the user request. Idiomatic pattern:

```text
# 1. Try Epic
epic(action="write_graph_dsl", asset=..., dsl=...)
# 2. If response says "toolset_not_available" or "operation_failed", re-route:
blueprint(action="read_graph_summary", ...)
blueprint(action="add_node", ...)
blueprint(action="connect_pins", ...)
blueprint(action="compile", ...)
```

## Why both exist

- **Native = guaranteed stable surface**, owned by us, predictable behavior
- **Epic = forward compatibility**, picks up new engine capabilities without bridge updates

Use both. Don't pick one.

## Cross-reference

- For DSL examples and grammar: see `ue-mcp-blueprint` "Authoring a graph body: prefer the Epic DSL" section
- For work that doesn't touch graphs (assets, levels, project ops): see `ue-mcp-workflow`
- For Bridge C++ extension when neither route covers an op: see `ue-mcp-native-cpp`
