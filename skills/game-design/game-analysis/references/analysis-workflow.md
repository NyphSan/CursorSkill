---
document_type: "Operational Workflow & Case Study"
source_material: "Rock Paper Scissors 2 (YouTube Video by Fractal Philosophy)"
target_audience: "Game Designers, System Architects"
parsing_instructions: "This document provides an actionable step-by-step workflow for applying theoretical game design concepts, followed by an end-to-end practical example."
---

# 1. The Intransitive Systems Workflow

This procedure allows designers to methodically audit an existing game loop or build a new one from scratch, ensuring that mathematical theory directly serves the player experience. It bridges the gap between abstract graph theory and playable mechanics.

## Phase 1: Decompose
* **Action:** Isolate the base entities.
* **Objective:** Identify the core "nodes" (e.g., unit types, elemental magic, combat stances) completely stripped of their statistical values, health bars, or secondary effects.

## Phase 2: Map
* **Action:** Define the interaction edges.
* **Objective:** Draw the win/loss/neutral matrix. Establish who beats whom in a mathematical vacuum to visualize the graph structure.

## Phase 3: Classify
* **Action:** Analyze the topology.
* **Objective:** Determine if the graph is transitive (linear power creep) or intransitive (cyclical). Check for symmetry (competitive balance) versus asymmetry (knowledge/roster checks).

## Phase 4: Locate
* **Action:** Find the prediction engine.
* **Objective:** Identify the exact mechanism forcing the player to guess. Is it simultaneous turns? Spatial positioning on a grid? Resource scarcity?

## Phase 5: Diagnose
* **Action:** Stress-test the math.
* **Objective:** Look for dominant strategies. Are there "Match" nodes that are strictly worse than others? Is there a combination of two nodes that eliminates all weaknesses (the "doom-stack" problem)?

## Phase 6: Propose Levers
* **Action:** Apply mechanical modifiers.
* **Objective:** Introduce layers to fix the diagnosis. Expand the roster to a 7-node "2-Paradox", add fog of war for information gathering, or restrict action economy to balance the scales.

---

# 2. End-to-End Worked Example: The Hex Crawler Strategy Game

To anchor output quality, we apply the workflow to a concrete scenario: designing the tactical combat loop for a dense hex-crawler strategy game (inspired by classics like *Heroes of Might and Magic*).

### Step 1: Decompose
We are building our core army roster. Stripping away all health, damage, and movement stats, we isolate four fundamental unit archetypes:
* Infantry (Shields)
* Cavalry (Charge)
* Ranged (Archers)
* Pikemen (Polearms)

### Step 2: Map
We define the interaction edges based on traditional logic:
* Pikemen beat Cavalry.
* Cavalry beat Ranged.
* Ranged beat Infantry.
* Infantry beat Pikemen.
* Pikemen and Ranged are neutral to each other.
* Infantry and Cavalry are neutral to each other.

### Step 3: Classify
Looking at the matrix, we have an **intransitive but incomplete** network. Because there are neutral spaces (no direct edges between certain units), this is not a strict "tournament" graph. It is slightly asymmetrical, meaning players can afford to make mistakes if they lock into a neutral engagement.

### Step 4: Locate
Because this is a turn-based hex crawler, the prediction engine is **spatial and resource-driven**, not simultaneous. The player is not blind-guessing what the AI will spawn; they are looking at the enemy army on the grid and predicting how the enemy will maneuver their units over the next three turns to gain flanking advantages.

### Step 5: Diagnose
During playtesting, a severe systemic weakness emerges. Because it is a 4-node system with neutral gaps, players discover a "doom-stack." If a player groups **Cavalry + Ranged** together, they cover each other's weaknesses perfectly. The Cavalry protects the Archers from Infantry, and the Archers shoot down the Pikemen before they can touch the Cavalry. The game state is "solved," the prediction engine dies, and the game becomes boring.

### Step 6: Propose Levers
To fix the doom-stack, we look to our game design levers:
* **The Math Lever (The 2-Paradox):** We recognize that a 4-node system allows for invincible two-unit combos. We expand the roster to 7 nodes by introducing Magic, Flying, and Siege units, carefully weaving their win/loss edges to create a mathematical 2-Paradox. Now, the Cavalry + Ranged stack has a definitive counter (e.g., Flying units bypass the Cavalry frontline, while Magic units strip the Ranged units of their accuracy).
* **The Information Lever (Fog of War):** We obscure the hex grid. The player can no longer perfectly calculate the enemy's formation on turn one. They must push fast, disposable Cavalry forward to scout.
* **The Resource Lever (Action Economy):** We limit movement points. Even if the player brings the perfect counter-unit, they must strategically sequence their turns to physically reach the target node on the hex grid before their own frontline collapses.

---

# 3. Methodological Note on the Worked Example (added 2026-07-06)

The Step 5 doom-stack conclusion is **matrix-valid**: no single node beats
both Cavalry and Ranged. In fact *every* pair in this 4-node graph is
unbeatable — the root weakness is the sparse 4-node structure itself, which
is exactly why the Step 6 expansion to a 7-node 2-Paradox is the right math
lever. Note, however, that the example's explanatory narrative ("the Cavalry
protects the Archers from Infantry, and the Archers shoot down the Pikemen")
invokes the **spatial layer**: per the matrix alone, Ranged already beats
Infantry, and Pikemen–Ranged is neutral. Lesson, codified as standing rule 1
of this skill: **diagnose the pure matrix first; any claim that leans on
space, tempo, or information must declare that layer explicitly.**

Also: this graph contains zero 3-cycles yet is intransitive (4-cycle
Infantry → Pikemen → Cavalry → Ranged → Infantry). Detecting intransitivity
therefore requires general cycle detection, not 3-cycle counting —
`scripts/matrix_analysis.py` does this.
