from utils import getInput, part1, part2
import numpy as np
import importlib
KnotHash = importlib.import_module("10").Processor  # Numeric file name


def as16byteStr(hex: str) -> str:
    # To avoid f-string within an f-string
    return f"{int(hex, 16):0128b}"


def solveDay() -> None:
    grid = list(map(lambda row: as16byteStr((KnotHash(f"{getInput(14, 2017).strip()}"
                                                      f"-{row}")).giveHash()),
                    range(128)))
    part1(sum(map(lambda row: row.count('1'), grid)))

    # Find all coordinates of ones in the grid
    ones = set(map(tuple,
                   np.array(np.where(np.array(list(map(lambda row: list(map(int,
                                                                            list(row))),
                                                       grid))))).T))

    # Count the regions
    regions = 0
    deltas = ((0, 1), (1, 0), (0, -1), (-1, 0))
    while ones:
        processed = set()
        adjacentToProcess = {ones.pop()}
        regions += 1
        while adjacentToProcess:
            r, c = adjacentToProcess.pop()
            processed.add((r, c))
            ones.discard((r, c))
            adjacentToProcess.update((ones & {(r + dr, c + dc) for dr, dc in deltas}))
    part2(regions)


solveDay()
