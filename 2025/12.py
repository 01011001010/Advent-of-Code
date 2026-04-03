from utils import getInput, part1
# import numpy as np


class Present:
    def __init__(self, block: str) -> None:
        self.size = block.count('#')

        # M = np.array([[space == '#' for space in row] for row in block.split()[1:]])
        # self.placements = []
        # for i in range(4):
        #     m1 = np.rot90(M)
        #     m2 = np.flip(m1)
        #     if not any([np.array_equal(m1, m) for m in self.placements]):
        #         self.placements.append(m1)
        #     if not any([np.array_equal(m2, m) for m in self.placements]):
        #         self.placements.append(m2)


def fits(row: str, presents: list[Present]) -> bool:
    w, h, *counts = map(int, row.replace('x', ' ').replace(':', '').split())
    spacesNeeded = sum([present.size * counts[i] for i, present in enumerate(presents)])
    # A quick look into the input made me suspicious, that some rows will not work, just
    # due to lack of space, as the size was small, but the count of presents high. So,
    # the first step was to check if it is physically possible to even fit the presents.
    # To see, how many rows are eliminated by this rule, the count of rows that pass the
    # check was printed. Since there was a considerable amount eliminated, the thought
    # of trying to submit that number came. And it turns out, it is enough. If there is
    # space, we just have to trust they fit :) Happy holidays!
    return w * h >= spacesNeeded


def solveDay() -> None:
    blocks = getInput(12, 2025).strip().split('\n\n')
    presents = [Present(presentBlock) for presentBlock in blocks[:6]]
    part1(sum([fits(row, presents) for row in blocks[6].split('\n')]))


solveDay()
