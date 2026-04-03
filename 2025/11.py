from utils import getInput, part1, part2


# a simple recursive counting of paths with memoisation
def countPaths(dest: str, parentDict: dict[str, str], memory: dict[str, int]) -> int:
    if dest not in memory:  # if not visited
        if dest not in parentDict:  # if not accessible
            memory[dest] = 0
        else:
            memory[dest] = sum([countPaths(parent, parentDict, memory)
                                for parent in parentDict[dest]])
    return memory[dest]


def solveDay() -> None:
    # initialise the network
    parentDict = {}
    for parent, *children in map(lambda line: line.replace(':', '').split(),
                                 getInput(11, 2025).strip().split('\n')):
        for child in children:
            if child not in parentDict:
                parentDict[child] = []
            parentDict[child].append(parent)

    # count the number of paths from `you` to `out`
    part1(countPaths('out', parentDict, {'you': 1}))

    # count the paths from `srv` to both of the choke-points, between them and to `out`
    # the total amount is simply the combination of the individual sections, minding
    # both allowed choke-point orders
    part2((countPaths('fft', parentDict, {'svr': 1})
           * countPaths('dac', parentDict, {'fft': 1})
           * countPaths('out', parentDict, {'dac': 1}))
          + (countPaths('dac', parentDict, {'svr': 1})
             * countPaths('fft', parentDict, {'dac': 1})
             * countPaths('out', parentDict, {'fft': 1})))


solveDay()
