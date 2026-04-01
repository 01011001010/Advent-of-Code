from utils import getInput, part1, part2
import networkx as nx


def solveDay() -> None:
    # Both puzzles on this day can be transformed into graph problems
    # Since there is no reason to reinvent a wheel, a graph library has been used

    # First, we load the map and the underlying graph
    lines = getInput(4, 2025).strip().split()
    rolls = {(x, y)
             for y, row in enumerate(lines)
             for x, roll in enumerate(row)
             if roll == '@'}

    # (N: rolls of paper, V: pairs of adjacent rolls)
    G = nx.Graph()
    for x, y in rolls:
        G.add_node((x, y))
        for neighbouring in {(x-1, y-1), (x, y-1), (x+1, y-1),
                             (x-1, y),             (x+1, y),
                             (x-1, y+1), (x, y+1), (x+1, y+1)}:
            if neighbouring in rolls:
                G.add_edge((x, y), neighbouring)

    # First part asks for rolls with less than 4 adjacent rolls
    # e.i. nodes with degree < 4
    part1(sum([deg < 4 for _, deg in G.degree()]))

    # Second part asks for all rolls, that can be removed (have less than 4 neighbours)
    # but allows incremental removal, allowing rolls to be uncovered with every removal
    # This task uses a 4-core subgraph, which by definition consists of nodes with
    # degree at least equal of 4 (counting only within the subgraph). The nodes in this
    # subgraph will never be uncovered, since they block each other. The 4-core will not
    # be removed, while the complement of the 4-core can be removed instantly or
    # incrementally. Thus the answer is the size of the graph - size of the 4-core.
    part2(G.number_of_nodes() - nx.k_core(G, 4).number_of_nodes())


solveDay()
