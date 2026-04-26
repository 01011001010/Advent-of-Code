from utils import getInput, part1, part2, RememberExtreme
from math import prod


class RememberQuantumEntanglement(RememberExtreme):
    def __init__(self, allGifts: list[int]) -> None:
        self.value = prod(allGifts)
        self.groupSize = len(allGifts)
        self.defaultStr = "Infinity"

    def newValueToConsider(self, value: set[int]) -> None:
        if len(value) < self.groupSize:
            self.groupSize = len(value)
            self.value = prod(value)
        elif len(value) == self.groupSize and (QE := prod(value)) < self.value:
            self.value = QE


def partition(gifts: list[int], partitions: int, partitionSize: int, firstSplit: bool,
              memory: RememberQuantumEntanglement) -> bool:
    group = set()
    complement = set(gifts)

    def backtrack(availableFromIndex: int) -> bool:
        for indexOffset, gift in enumerate(gifts[availableFromIndex:]):
            group.add(gift)
            complement.remove(gift)
            currentSum = sum(group)
            if currentSum == partitionSize:  # A correctly sized group was created
                if firstSplit:
                    # First group is separated, as we want to continue even if valid
                    if partition(sorted(complement, reverse=True),
                                 partitions - 1,
                                 partitionSize,
                                 False,
                                 memory):
                        memory.newValueToConsider(group)
                elif partitions == 2:
                    # Splitting into half
                    # We are kinda relying, that the sum of gifts equals
                    # (`partitions` * `partitionSize`) for any outside call, then we do
                    # not need to check here
                    return True
                else:
                    # We need to see, if the complement group can be partitioned
                    return partition(sorted(complement, reverse=True),
                                     partitions - 1,
                                     partitionSize,
                                     False,
                                     memory)

            elif currentSum < partitionSize:  # Our group is not big enough
                if firstSplit:
                    if memory.groupSize > len(group):  # Not worth looking if too big
                        # Not returning any value, as we want to keep iterating over all
                        # partitions
                        backtrack(availableFromIndex + indexOffset + 1)
                else:
                    if backtrack(availableFromIndex + indexOffset + 1):
                        return True

            group.remove(gift)
            complement.add(gift)

        return False

    return backtrack(0)


def solveDay() -> None:
    gifts = sorted(map(int, getInput(24, 2015).strip().split('\n')), reverse=True)

    for groups, part in (3, part1), (4, part2):
        quantumEntanglement = RememberQuantumEntanglement(gifts)
        partition(gifts, groups, sum(gifts) // groups, True, quantumEntanglement)
        part(quantumEntanglement.getValue())


solveDay()
