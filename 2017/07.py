from utils import getInput, part1, part2
import numpy as np
from re import findall


class Program:
    def __init__(self, name: str) -> None:
        self.weight = None
        self.above = None
        self.below = None
        self.name = name

    def setBelow(self, other: "Program") -> None:
        self.below = other

    def setWeight(self, weight: int) -> None:
        self.weight = weight

    def setAbove(self, above: tuple["Program"]) -> None:
        self.above = above

    def getBottom(self) -> "Program":
        if self.below is None:
            return self
        return self.below.getBottom()

    def balance(self) -> np.ndarray:
        # Investigate weights of sub-towers.
        # If the sub-sub towers, the second position indicates their weights.
        # If there is an imbalance, the corrected weight is propagated through the first
        # position.
        if self.above is None:
            return np.array([0, self.weight])
        subTowers = np.array([program.balance() for program in self.above])
        if subTowers[:, 0].sum() != 0:
            return subTowers.sum(axis=0)
        if len(set(subTowers[:, 1])) == 1:
            return np.array([0, subTowers[:, 1].sum() + self.weight])
        else:
            if len(self.above) == 2:
                raise NotImplementedError("Imbalance occurs at 2 branches.")
            else:
                smallest = subTowers[:, 1].min()
                largest = subTowers[:, 1].max()

                smallestIndex = np.where(subTowers[:, 1] == smallest)[0]
                largestIndex = np.where(subTowers[:, 1] == largest)[0]

                smallIsOddOneOut = len(smallestIndex) == 1

                index = smallestIndex[0] if smallIsOddOneOut else largestIndex[0]
                return np.array([(self.above[index].weight + ((largest - smallest)
                                                              * (1
                                                                 if smallIsOddOneOut
                                                                 else -1))),
                                 0])


def constructTowerAndGetBottom() -> Program:
    name = None
    programs = {}
    for yellOut in getInput(7, 2017).strip().splitlines():
        name, weight, *above = findall(r"\w+", yellOut)
        if name not in programs:
            programs[name] = Program(name)

        for programAbove in above:
            programs[programAbove] = programs.get(programAbove, Program(programAbove))
            programs[programAbove].setBelow(programs[name])

        programs[name].setAbove(tuple(map(lambda name: programs[name], above)))
        programs[name].setWeight(int(weight))

    if name is None:
        raise ValueError("No programmes were recognised in the puzzle input")

    return programs[name].getBottom()


def solveDay() -> None:
    part1((bottom := constructTowerAndGetBottom()).name)
    part2(bottom.balance()[0])


solveDay()
