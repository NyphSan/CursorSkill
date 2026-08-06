---
document_type: "Systems Analysis & Game Design Document"
source_material: "Rock Paper Scissors 2 (YouTube Video by Fractal Philosophy)"
target_audience: "AI Agents, LLMs, Game Designers, System Architects"
parsing_instructions: "This document is structured using semantic headers and distinct conceptual blocks for optimal Retrieval-Augmented Generation (RAG) chunking and context ingestion."
---

# 1. System Overview: The Core Philosophy of Game Mechanics

## 1.1. The Atomic Unit of Prediction
At a fundamental mathematical and psychological level, games function as engines for **prediction and decision-making**. The traditional game of Rock-Paper-Scissors (RPS) serves as the atomic unit of this concept. The objective utility of a game is not found in mathematical optimization of a single dominant strategy, but in the psychological friction of anticipating an opponent's behavior within a constrained system.

## 1.2. Pillars of the Prediction Engine
To successfully force an unpredictable, skill-based psychological loop, a system relies on three interacting mechanisms:
* **Simultaneous Action (Zero-Reactivity):** Actions must resolve concurrently. If turns are sequential without hidden information, the system devolves into deterministic reaction (e.g., standard chess mechanics where absolute information is present).
* **Balanced Intransitive Networks:** The state-space must consist of cyclical advantages (A > B > C > A) rather than linear, transitive hierarchies (A > B > C). This ensures a mathematical equilibrium where no node possesses dominant objective value, shifting the burden of victory from system exploitation to opponent prediction.
* **Network Constraint (Low Cognitive Load):** The subset of immediately available choices must remain small. Massive option pools dilute the psychological focus, forcing the agent (human or AI) to expend computational power memorizing node-interactions rather than analyzing behavioral patterns.

---

# 2. Architectural Design Modifiers (Layering Complexity)

To build fully-fledged game architectures, designers take the atomic RPS unit and superimpose mechanical layers. These layers manipulate how actors gather state-information and alter the exact type of predictions being made.

## 2.1. Iteration and the Law of Large Numbers
* **Mechanic:** Multi-round resolution (e.g., "Best 2 out of 3").
* **Systemic Effect:** Transforms a game of pure chance into one of pattern recognition. Over successive iterations, agents generate behavioral data. Predictions shift from "What is the optimal move?" to "What is this specific actor's frequency bias based on prior states?"

## 2.2. Resource Scarcity and State-Dependent Weighting
* **Mechanic:** Limiting node selection (e.g., a hand of 3 Rocks, 1 Paper, 0 Scissors).
* **Systemic Effect:** Assigns dynamic economic weight to decisions. The probability of an actor choosing "Paper" shifts drastically depending on whether it is their abundant resource or their final trump card.

## 2.3. Spatial Dynamics and Grid Translation
* **Mechanic:** Projecting intransitive relationships onto a geographical state-space (e.g., dense hex crawlers, tactical grids, real-time strategy deployment).
* **Systemic Effect:** Shifts the required prediction horizon. Immediate tactical prediction is replaced by long-term strategic positioning, evaluating terrain control, movement vectors, and multi-unit synergy over time.

## 2.4. Asymmetric Complexity (Knowledge Checks)
* **Mechanic:** Intentionally breaking mathematical equilibrium to create highly sparse or unbalanced interaction matrices (e.g., 18 elemental types with distinct immunities and resistances).
* **Systemic Effect:** Appeals to system-mastery and categorization rather than pure psychological reading. Viability must be discovered or mathematically calculated, creating a meta-game of optimization and team-building.

## 2.5. The 2-Paradox (Advanced Networking)
* **Mechanic:** A 7-node mathematical graph where *every combination of two nodes* is defeated by at least one other node.
* **Systemic Effect:** Completely eliminates the concept of an invincible composition. It forces continuous adaptation, making it impossible to statically solve the game state. In campaign or tabletop structures, these networks can be subset—for instance, Act 1 features a single element, Act 2 introduces a standard 3-node RPS triangle, and Act 3 expands into the full 7-node 2-Paradox, allowing the narrative scaling to match the mechanical escalation.

---

# 3. Analytical Frameworks (Evaluating Game Typology)

AI agents and designers can classify and solve game loops by analyzing their structural properties.

## 3.1. Evaluating Transitivity
* **Method:** Map the interaction edges.
* **Analysis:** If the graph flows in one direction (A > B, B > C, therefore A > C), the game is **Transitive** (progression-based, linear scaling, "stat checks"). If the graph loops, it is **Intransitive** (strategy-based, situational utility).

## 3.2. Evaluating Turn Pacing
* **Method:** Observe execution timing.
* **Analysis:** Simultaneous execution rewards immediate psychological profiling. Sequential (turn-based) execution with spatial elements rewards resource allocation and long-term planning trees.

## 3.3. Evaluating Symmetry
* **Method:** Analyze the interaction matrix for null or mirrored values.
* **Analysis:** A dense, perfectly mirrored matrix (Win/Loss) defines a competitive prediction game. A sparse, asymmetrical matrix (featuring varying damage multipliers or neutral states) defines a game centered around roster construction, knowledge checks, and progressive mastery.

## 3.4. Eigenvector Centrality (Matrix Math)
* **Method:** Convert the game's type-effectiveness chart into a linear transformation matrix. Use computational engines (like Wolfram Alpha or numpy/scipy) to solve for the matrix's eigenvectors.
* **Analysis:** This mathematical formulation calculates the "true" underlying viability of different elements within an unbalanced game by measuring the steady-state probabilities of node dominance.

---

# 4. Epistemological Journey: Key Questions & Methodologies

This section traces the logical deduction used to deconstruct and rebuild the mechanics of Rock Paper Scissors.

### Query 1: The Question of Scale
* **Hypothesis:** Expanding RPS to 15, 25, or 101 options improves the game.
* **Conclusion:** False. While maintaining mathematical fairness (50% win/loss ratio), hyper-scaling destroys the user experience. The cognitive load required to parse interactions overrides the psychological prediction loop.
* **Methodology:** Psychological design analysis—prioritizing human cognitive constraints over pure mathematical geometry.

### Query 2: The Question of Appeal
* **Hypothesis:** The pure random chance of RPS is the source of engagement.
* **Conclusion:** False. RPS is fun because it is a prediction engine fueled by out-of-band social manipulation (bluffing, rhetoric, behavioral tells) which allows players to collapse probabilities.
* **Methodology:** Theoretical deconstruction (removing rules to see what breaks) combined with observational analysis of real-world meta-gaming behavior.

### Query 3: The Question of Practical Improvement
* **Hypothesis:** The base game can be evolved without losing its core identity.
* **Conclusion:** True. It is evolved by integrating iteration, resource management, and spatial topography.
* **Methodology:** Empirical case study analysis—analyzing successful implementations in external media (e.g., *Total War* unit tactics, *Kaiji* resource scarcity).

### Query 4: The Question of the "Holy Grail" System
* **Hypothesis:** It is possible to build a fully balanced RPS system where no combination of two elements is safe from a counter.
* **Conclusion:** True. This requires a specific graph structure called a 2-Paradox, which necessitates a minimum of exactly 7 nodes.
* **Methodology:** Mathematical translation. By converting abstract game design rules into the formal nomenclature of **Graph Theory** (Nodes, Edges, Tournaments), the problem became searchable in academic mathematical literature, yielding the proven 7-node minimum.

---

# 5. Glossary of Systemic & Mathematical Terms

* **Transitive Relationship:** A hierarchical logical sequence where relational advantages stack and carry over (e.g., A > B, and B > C → A > C).
* **Intransitive Network:** A cyclical, closed-loop network without a strict apex element; advantages are entirely contextual.
* **Law of Large Numbers:** A theorem in probability stating that the average of results obtained from a large number of trials converges upon the expected mathematical value.
* **Graph Theory:** The mathematical study of graphs, which are structures used to model pairwise relations between objects (highly applicable for mapping state-machines and multi-agent systems).
* **Node (Vertex):** A fundamental discrete unit, option, or state within a graph (e.g., the "Fire" element, or a specific tactical unit).
* **Edge (Link/Line):** The directional, logical connection between two nodes detailing their interaction (e.g., the rule vector defining that Water damages Fire).
* **Graph:** The holistic macro-structure formed by the entirety of a system's nodes and their interconnecting edges.
* **Tournament:** A specific classification of a directed graph where every single node has an edge connecting it to every other node (meaning all matchups resolve in a strict win/loss, with zero neutral or tie states).
* **Paradoxical Tournament (1-Paradox):** A tournament graph where every distinct node is defeated by at least one other node (the foundation of standard RPS).
* **2-Paradox:** A highly complex mathematical tournament configuration where *every possible subset of two nodes* is defeated by at least one other node. The mathematically absolute smallest version requires 7 nodes.
* **Eigenvector:** A non-zero vector that changes at most by a scalar factor when a linear transformation is applied to it. In game design, it is extracted from a damage-multiplier matrix to compute the objective scalar power of asymmetrical game pieces.

---

# 6. Errata & Scope Notes (added 2026-07-06, project decision)

* **"Match" nodes** (companion workflow doc, Phase 5) is a transcription
  artifact from the source video. Read as **dominated nodes**: node Y
  dominates node X when Y's outcome is at least as good as X's against every
  opponent column (self-matchups neutral) and strictly better against at
  least one.
* **Scope:** the frameworks in this document target a game's *interaction
  core* (node-vs-node counterplay). Fun taxonomy beyond the prediction engine
  lives in `fun-engines.md`; levers beyond the interaction core live in
  `systemic-levers.md`.
