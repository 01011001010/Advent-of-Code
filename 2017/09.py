from utils import getInput, part1, part2
import numpy as np


def countScoreAndGarbage(line: str) -> tuple[int, int]:
    # So many memories of automata, almost tempted to define this one in formal terms
    openGroups = 0
    score = 0
    garbage = 0
    skipNext = False
    isGarbage = False

    for char in line:
        if skipNext:
            skipNext = False
            continue
        if not isGarbage and char == '{':
            openGroups += 1
        elif not isGarbage and char == '}':
            score += openGroups
            openGroups -= 1
        elif not isGarbage and char == '<':
            isGarbage = True
        elif char == '>':
            isGarbage = False
        elif char == '!':
            skipNext = True
        elif isGarbage:
            garbage += 1

    return score, garbage


def solveDay() -> None:
    score, garbage = np.array(list(map(countScoreAndGarbage,
                                       getInput(9, 2017).strip().splitlines()))
                              ).sum(axis=0)
    part1(score)
    part2(garbage)


solveDay()
