from utils import getInput, part1, part2


def initialiseDistances() -> dict[str, dict[str, int]]:
    specifications = getInput(9, 2015).strip().splitlines()
    distances = {}
    for spec in specifications:
        origin, destination, distance = spec.replace("to", "=").strip().split(' = ')
        distances[origin] = distances.get(origin, dict())
        distances[destination] = distances.get(destination, dict())
        distances[origin][destination] = distances[destination][origin] = int(distance)
    return distances


def evaluateAllCycles(start: str, lastVisited: str, distancesTravelled: tuple[int, ...],
                      notVisitedYet: tuple, distances: dict[str, dict[str, int]],
                      short: list, long:  list) -> None:
    # construct all possible Hamiltonian paths in the graph with the given start
    if notVisitedYet:
        for i, visiting in enumerate(notVisitedYet):
            evaluateAllCycles(start,
                              visiting,
                              distancesTravelled + (distances[visiting][lastVisited],),
                              notVisitedYet[:i] + notVisitedYet[i+1:],
                              distances,
                              short,
                              long)
    else:
        # close the Hamiltonian path into a Hamiltonian cycle
        distancesTravelled += (distances[start][lastVisited],)

        # exclude the longest/shortest edge for shortest/longest Hamiltonian path
        short.append(min(short, sum(distancesTravelled) - max(distancesTravelled)))
        long.append(max(long, sum(distancesTravelled) - min(distancesTravelled)))


def solveDay() -> None:
    distances = initialiseDistances()
    shortest = []
    longest = []

    # as we look at loops, one starting point is enough
    evaluateAllCycles('AlphaCentauri',
                      'AlphaCentauri',
                      (),
                      tuple(distances['AlphaCentauri'].keys()),
                      distances,
                      shortest,
                      longest)

    part1(min(shortest))
    part2(max(longest))


solveDay()
