from utils import getInput, part1, part2
from re import findall
from math import gcd, inf


def searchForNotDetected(maxDepth: int | float = inf,
                         maxDelay: int = int(10e10), returnFirst: bool = True,
                         step: int = 1,
                         returnSeverity: bool = False) -> tuple[int, list[int]]:
    scanners = {(depth, layerRange)
                for depth, layerRange
                in map(lambda info: map(int, findall(r"\d+", info)),
                       getInput(13, 2017).strip().splitlines())}

    notDetected = []
    severity = 0
    for delay in range(0, maxDelay, step):
        breach = False
        for depth, layerRange in filter(lambda p: p[0] <= maxDepth,
                                        sorted(scanners, key=lambda p: p[1])):
            if (delay + depth) % ((layerRange - 1) * 2) == 0:
                breach = True
                if returnSeverity:
                    severity += layerRange * depth
                else:
                    break
        if returnSeverity:
            return severity, []
        if breach:
            continue
        if returnFirst:
            return delay, []
        notDetected.append(delay)
    return 0, notDetected


def severity() -> int:
    return searchForNotDetected(returnSeverity=True)[0]


def smallestDelay() -> int:
    # with a subset of scanners, find a frequency that they let through and then
    # condense the search set for computing the full answer
    return searchForNotDetected(step=gcd(*(searchForNotDetected(60, 100000, False)[1]))
                                )[0]


def solveDay() -> None:
    part1(severity())
    part2(smallestDelay())


solveDay()
