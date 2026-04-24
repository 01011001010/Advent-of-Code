import re
from utils import getInput, part1


def codeIndex(row: int, col: int) -> int:
    return (((row + col - 1) * (row + col - 2) // 2)  # sum of 1 -> row+col-2 inclusive
            + col)  # plus the position on the (row+col-1)th diagonal


def codeAtIndex(idx: int) -> int:
    # My original solution looked for loops in the code sequence (the moment a code
    # repeats, we entered a loop). The loop occurred much later than the required code.
    # The loop search portion was therefore removed.
    assert idx > 0, f"Codes are indexed by natural numbers. {idx} is an invalid index."
    code = 20151125
    for _ in range(1, idx):
        code = (code * 252533) % 33554393
    return code


def solveDay() -> None:
    part1(codeAtIndex(codeIndex(*map(int,
                                     re.findall(r"\d+", getInput(25, 2015).strip())))))


solveDay()
