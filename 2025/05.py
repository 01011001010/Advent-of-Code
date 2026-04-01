from utils import getInput, part1, part2
from typing import Self


class Range:  # single continuous range of fresh IDs
    def __init__(self, lower: int, upper: int) -> None:
        self.combined = False  # flag to invalidate ranges consumed by others
        self.lower = lower  # lowest fresh ID
        self.upper = upper  # highest fresh ID
        self.len = upper - lower + 1  # size of the range (count of fresh IDs)

    def combine(self, other: Self) -> None:
        if self.combined or other.combined:  # skip already absorbed ranges
            return
        if other < self:  # if `other`'s lower boundary is smaller, combine into it
            other.combine(self)
            return
        if self.upper >= other.lower:  # if overlapping or adjacent
            other.combined = True  # mark `other` as absorbed
            self.upper = max(self.upper, other.upper)  # find the upper boundary
            self.len = self.upper - self.lower + 1  # adjust size

    def containsID(self, id: int) -> bool:  # check if the ID is contained in this range
        return self.lower <= id <= self.upper

    def __len__(self) -> int:  # size of the range; 0 if it has been absorbed by another
        return 0 if self.combined else self.len

    def __lt__(self, other: Self) -> bool:  # compare lower boundaries of the two ranges
        return self.lower < other.lower

    def wasNotCombined(self) -> bool:
        return not self.combined


class Ranges:  # collection of all ID ranges
    def __init__(self, rawBlock: str) -> None:
        # parse the string input to Range objects
        # sort the ranges by their lower boundaries
        self.ranges = sorted(map(lambda line: Range(*map(int, line.split('-'))),
                                 rawBlock.strip().split()))

        # combine overlapping or adjacent ranges
        for i, rng in enumerate(self.ranges):
            for rngOther in self.ranges[i+1:]:
                rng.combine(rngOther)

        # discard absorbed ranges
        self.ranges = list(filter(Range.wasNotCombined, self.ranges))

    def isFresh(self, id: int) -> bool:
        # check if the ID is contained in
        for rng in self.ranges:
            if rng.containsID(id):
                return True
            if rng.lower > id:  # this works thanks to the sorting of the ranges
                return False
        return False

    def countFresh(self, rawBlock: str) -> int:
        # parse the raw input; check if ID is fresh; count up
        return sum([self.isFresh(id) for id in map(int, rawBlock.strip().split())])

    def countAllFreshIDs(self) -> int:
        # sum up the sizes of all ranges
        # works this simply thanks to range combination in the constructor
        return sum(map(len, self.ranges))


def solveDay() -> None:
    rangeBlock, IDBlock = getInput(5, 2025).strip().split('\n\n')
    ranges = Ranges(rangeBlock)

    part1(ranges.countFresh(IDBlock))
    part2(ranges.countAllFreshIDs())


solveDay()
