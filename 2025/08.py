from utils import getInput, part1, part2
import networkx as nx
from typing import Self


class JunctionBox:  # Easy management entity management and distance calculation
    def __init__(self, line: str) -> None:
        self.x, self.y, self.z = map(int, line.split(','))

    def distSqr(self, other: Self) -> int:
        return ((self.x - other.x) ** 2 +
                (self.y - other.y) ** 2 +
                (self.z - other.z) ** 2)


def solveDay() -> None:
    rows = getInput(8, 2025).strip().split()

    junctionBoxes = [JunctionBox(row) for row in rows]
    # calculate the distance for each pair of junction boxes and sort by the distance
    sortedDists = sorted([((i, j), junctionBoxes[i].distSqr(junctionBoxes[j]))
                          for i in range(len(junctionBoxes))
                          for j in range(len(junctionBoxes))
                          if i < j],
                         key=lambda pair: pair[1])

    # create a graph with nodes being all the junction boxes
    G = nx.Graph()
    # and add the 1000 shortest edges
    for (i, j), _ in sortedDists[:1000]:
        G.add_edge(i, j)

    # find the sizes of the 3 largest connected components
    circuits = sorted((len(g) for g in nx.connected_components(G)), reverse=True)[:3]
    part1(circuits[0] * circuits[1] * circuits[2])

    # Since we do not care bout the skeleton distances, just which edge ensures the
    # full-network connectivity, we do not need to construct the skeleton. We can just
    # keep adding edges until we have one fully-connected component.
    i, j = None, None
    for (i, j), _ in sortedDists[1000:]:
        G.add_edge(i, j)
        # Since we did not add all the nodes at the beginning, we need to check, if we
        # all junction boxes have been added (along with the edges).
        #
        # When we have all the nodes and one component in the graph, we are done
        #
        # This condition is an ugly brute force, and tracking component affiliation with
        # every edge addition is much nicer. This solution, however, works fast anyway.
        # I might come back at some point to implement a nicer version.
        if G.number_of_nodes() == len(rows) and len([nx.connected_components(G)]) == 1:
            break

    assert i is not None and j is not None, ("The loop did not run, check "
                                             "sortedDists[1000:] to see why")
    part2(junctionBoxes[i].x * junctionBoxes[j].x)


solveDay()
