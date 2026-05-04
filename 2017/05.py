from utils import getInput, part1, part2
from typing import Callable


class Pointer:
    def __init__(self) -> None:
        self.position = 0
        self.jumpCount = 0

    def jumpBy(self, offset: int) -> None:
        self.jumpCount += 1
        self.position += offset


def oneJumpAndSeeIfInside(jumpOffsets: list[int], pointer: Pointer,
                          changeFunction: Callable) -> bool:
    jumpingFromPosition = pointer.position
    pointer.jumpBy(jumpOffsets[jumpingFromPosition])

    jumpOffsets[jumpingFromPosition] = changeFunction(jumpOffsets[jumpingFromPosition])

    return 0 <= pointer.position < len(jumpOffsets)


def jumpsToEscape(offsetChangeFunction: Callable) -> int:
    pointer = Pointer()
    jumpOffsets = list(map(int, getInput(5, 2017).strip().splitlines()))
    while oneJumpAndSeeIfInside(jumpOffsets, pointer, offsetChangeFunction):
        pass
    return pointer.jumpCount


def solveDay() -> None:
    part1(jumpsToEscape(lambda offset: offset + 1))

    # Part 2 can surely be solved in a cleverer way, but this is fast enough ¯\_(ツ)_/¯
    part2(jumpsToEscape(lambda offset: offset + 1 if offset < 3 else offset - 1))


solveDay()
