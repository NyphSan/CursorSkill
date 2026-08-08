#!/usr/bin/env python3
"""Diagnostics for game interaction matrices (Python 3 stdlib only).

Input JSON: {"nodes": [...], "matrix": [[...]]}; matrix[i][j] is row-vs-column.
Binary mode (values in {-1, 0, 1}): 1 = row beats column, -1 = loses, 0 = neutral.
Weighted mode (anything else, e.g. effectiveness multipliers): i beats j iff
matrix[i][j] > matrix[j][i]; diagonal entries are ignored (self-matchup neutral).

Known limitations: a weighted/effectiveness matrix whose values happen to fall
entirely within {-1, 0, 1} will be auto-detected as binary mode; disambiguate
manually if a weighted matrix is unexpectedly rejected by binary-mode validation.
Weighted-mode eigenvector centrality uses the raw effectiveness values, so scores
are not comparable across games that use different multiplier scales.
Weighted matrices with negative values: outcome semantics (i beats j iff
matrix[i][j] > matrix[j][i]) remain valid, but eigenvector centrality is skipped
— power iteration assumes non-negative weights, and signed encodings of the same
game can invert or corrupt the scores. Prefer a non-negative encoding (points
scored, effectiveness multipliers) when viability scores are wanted.
"""
import argparse
import itertools
import json
import math
import sys


def load_input(path):
    with open(path) as f:
        data = json.load(f)
    if not isinstance(data, dict) or "nodes" not in data or "matrix" not in data:
        raise ValueError('Input must be a JSON object with "nodes" and "matrix" keys.')
    nodes, matrix = data["nodes"], data["matrix"]
    if not isinstance(nodes, list) or not isinstance(matrix, list):
        raise ValueError('"nodes" and "matrix" must both be lists.')
    n = len(nodes)
    if n == 0:
        raise ValueError("nodes must be non-empty.")
    if any(not isinstance(name, str) for name in nodes):
        raise ValueError("node names must be strings.")
    if len(set(nodes)) != n:
        raise ValueError("node names must be unique.")
    if any(not isinstance(row, list) for row in matrix):
        raise ValueError("matrix rows must be lists.")
    if len(matrix) != n or any(len(row) != n for row in matrix):
        raise ValueError(f"matrix must be {n}x{n} to match nodes.")
    for row in matrix:
        for v in row:
            if isinstance(v, bool) or not isinstance(v, (int, float)):
                raise ValueError("matrix values must be numbers.")
    values = {v for row in matrix for v in row}
    mode = "binary" if values <= {-1, 0, 1} else "weighted"
    if mode == "binary":
        for i in range(n):
            if matrix[i][i] != 0:
                raise ValueError(f"binary mode: diagonal must be 0 (node {nodes[i]}).")
            for j in range(n):
                if matrix[j][i] != -matrix[i][j]:
                    raise ValueError(
                        f"binary mode: antisymmetry violated at {nodes[i]} vs {nodes[j]}.")
    return nodes, matrix, mode


def outcome(matrix, mode, i, j):
    """1 if i beats j, -1 if i loses, 0 if neutral. Diagonal is always neutral."""
    if i == j:
        return 0
    if mode == "binary":
        return matrix[i][j]
    if matrix[i][j] > matrix[j][i]:
        return 1
    if matrix[i][j] < matrix[j][i]:
        return -1
    return 0


def beats_graph(nodes, matrix, mode):
    n = len(nodes)
    return {i: {j for j in range(n) if outcome(matrix, mode, i, j) == 1}
            for i in range(n)}


def is_tournament(nodes, matrix, mode):
    n = len(nodes)
    return all(outcome(matrix, mode, i, j) != 0
               for i in range(n) for j in range(n) if i != j)


def find_cycle(graph, n):
    """Return one directed cycle as a list of node indices, or None if acyclic."""
    color = [0] * n  # 0 white, 1 gray, 2 black
    parent = [None] * n
    result = []

    def dfs(u):
        color[u] = 1
        for v in sorted(graph[u]):
            if color[v] == 0:
                parent[v] = u
                if dfs(v):
                    return True
            elif color[v] == 1:  # back-edge: cycle v -> ... -> u -> v
                cyc = [u]
                while cyc[-1] != v:
                    cyc.append(parent[cyc[-1]])
                cyc.reverse()
                result[:] = cyc
                return True
        color[u] = 2
        return False

    for s in range(n):
        if color[s] == 0 and dfs(s):
            return result
    return None


def topological_order(graph, n):
    """Kahn's algorithm; returns the order, or None if the graph has a cycle."""
    indeg = [0] * n
    for i in range(n):
        for j in graph[i]:
            indeg[j] += 1
    queue = sorted(i for i in range(n) if indeg[i] == 0)
    order = []
    while queue:
        u = queue.pop(0)
        order.append(u)
        for v in sorted(graph[u]):
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
        queue.sort()
    return order if len(order) == n else None


def three_cycle_count(graph, n):
    count = 0
    for i, j, k in itertools.combinations(range(n), 3):
        if (j in graph[i] and k in graph[j] and i in graph[k]) or \
           (k in graph[i] and j in graph[k] and i in graph[j]):
            count += 1
    return count


def dominated_nodes(nodes, matrix, mode):
    """(dominated, dominator) pairs. Y dominates X iff outcome(Y,k) >= outcome(X,k)
    for EVERY column k (self-matchups neutral), strictly better for at least one."""
    n = len(nodes)
    found = []
    for x in range(n):
        for y in range(n):
            if x == y:
                continue
            ge = all(outcome(matrix, mode, y, k) >= outcome(matrix, mode, x, k)
                     for k in range(n))
            gt = any(outcome(matrix, mode, y, k) > outcome(matrix, mode, x, k)
                     for k in range(n))
            if ge and gt:
                found.append((nodes[x], nodes[y]))
    return found


def doom_stacks(nodes, matrix, mode, k):
    """All unbeatable k-subsets; None if the search space exceeds the guard."""
    n = len(nodes)
    if k > n:
        return []
    if math.comb(n, k) > 20000:
        return None
    stacks = []
    for subset in itertools.combinations(range(n), k):
        beatable = any(all(outcome(matrix, mode, z, s) == 1 for s in subset)
                       for z in range(n) if z not in subset)
        if not beatable:
            stacks.append(tuple(nodes[s] for s in subset))
    return stacks


def eigenvector_centrality(nodes, matrix, mode, damping=0.01, tol=1e-9, max_iter=200):
    """Steady-state viability heuristic (power iteration), L1-normalized, ranked.

    Returns None for weighted matrices containing negative off-diagonal values:
    power iteration assumes non-negative weights, and signed encodings (e.g. a
    zero-sum differential chart) produce meaningless, even negative, scores."""
    n = len(nodes)
    if mode == "weighted" and any(matrix[i][j] < 0
                                  for i in range(n) for j in range(n) if i != j):
        return None
    if mode == "binary":
        weight = {1: 1.0, 0: 0.5, -1: 0.0}
        A = [[0.5 if i == j else weight[outcome(matrix, mode, i, j)]
              for j in range(n)] for i in range(n)]
    else:
        A = [[1.0 if i == j else float(matrix[i][j]) for j in range(n)]
             for i in range(n)]
    A = [[A[i][j] + damping for j in range(n)] for i in range(n)]
    v = [1.0 / n] * n
    for _ in range(max_iter):
        w = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
        total = sum(w)
        w = [x / total for x in w]
        if max(abs(w[i] - v[i]) for i in range(n)) < tol:
            v = w
            break
        v = w
    return sorted(zip(nodes, v), key=lambda t: (-t[1], t[0]))


def format_report(nodes, matrix, mode, max_stack):
    n = len(nodes)
    lines = [f"Mode: {mode} | Nodes: {n} ({', '.join(nodes)})", ""]

    lines.append("== STRUCTURE ==")
    lines.append(f"Tournament: {'yes' if is_tournament(nodes, matrix, mode) else 'no'}"
                 " (tournament = every matchup has a winner)")
    graph = beats_graph(nodes, matrix, mode)
    cycle = find_cycle(graph, n)
    if cycle is None:
        order = topological_order(graph, n)
        hierarchy = " > ".join(nodes[i] for i in order)
        lines.append(f"TRANSITIVE (beats-graph is acyclic). Power hierarchy: {hierarchy}")
    else:
        shown = " -> ".join(nodes[i] for i in cycle) + f" -> {nodes[cycle[0]]}"
        lines.append(f"INTRANSITIVE (cycle exists). Example cycle: {shown}")
    lines.append(f"3-cycles: {three_cycle_count(graph, n)}")
    lines.append("")

    lines.append("== DOMINATED NODES ==")
    dom = dominated_nodes(nodes, matrix, mode)
    if not dom:
        lines.append("Dominated nodes: none")
    else:
        for x, y in dom:
            lines.append(f"{x} is DOMINATED by {y} (never a better pick).")
    lines.append("")

    lines.append("== DOOM-STACKS (unbeatable subsets) ==")
    for k in range(2, max_stack + 1):
        stacks = doom_stacks(nodes, matrix, mode, k)
        if stacks is None:
            lines.append(f"size {k}: skipped (search space over guard limit).")
        elif not stacks:
            lines.append(f"size {k}: none — the "
                         f"{'2-Paradox property holds' if k == 2 else f'{k}-subset property holds'}.")
        else:
            lines.append(f"{len(stacks)} unbeatable subset(s) of size {k}"
                         + (" — 2-Paradox property does NOT hold:" if k == 2 else ":"))
            for s in stacks:
                lines.append(f"  {s}")
    lines.append("")

    lines.append("== VIABILITY (eigenvector centrality, steady-state heuristic) ==")
    ranked = eigenvector_centrality(nodes, matrix, mode)
    if ranked is None:
        lines.append("  skipped — weighted matrix contains negative values; power-iteration")
        lines.append("  viability assumes non-negative weights. Re-encode the chart")
        lines.append("  non-negatively (points scored / effectiveness multipliers) for scores.")
    else:
        for name, score in ranked:
            lines.append(f"  {name}: {score:.4f}")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Diagnostics for game interaction matrices.")
    parser.add_argument("input", help="JSON file with 'nodes' and 'matrix'")
    parser.add_argument("--max-stack", type=int, default=2, choices=[2, 3],
                        help="largest doom-stack subset size to search")
    args = parser.parse_args(argv)
    try:
        nodes, matrix, mode = load_input(args.input)
    except (OSError, json.JSONDecodeError, ValueError) as e:
        print(f"INPUT ERROR: {e}", file=sys.stderr)
        return 1
    print(format_report(nodes, matrix, mode, args.max_stack))
    return 0


if __name__ == "__main__":
    sys.exit(main())
