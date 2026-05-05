from utils import getInput, part1, part2
import numpy as np


def redistribute(memoryBanks: np.ndarray) -> None:
    index = np.argmax(memoryBanks)
    lengthOfMemory = memoryBanks.shape[0]
    (np.concatenate((memoryBanks,  # previous state
                     np.full(index, 0),  # nothing until the redistributed bank
                     (-memoryBanks[index],),  # take fom the redistributed bank
                     np.full(memoryBanks[index], 1),  # spread the value
                     np.full((- (index + 1 + memoryBanks[index]))
                             % lengthOfMemory, 0))  # pad till end with 0
                    ).reshape((-1, memoryBanks.shape[0]))  # reshape into rows
     ).sum(axis=0, out=memoryBanks)  # sum over columns


def redistributeTillRepeatState(memoryBanks: np.ndarray) -> tuple[int, int]:
    cycleCounter = 0
    seenAt = {tuple(memoryBanks): cycleCounter}
    while True:
        cycleCounter += 1
        redistribute(memoryBanks)
        if (state := tuple(memoryBanks)) in seenAt:
            return seenAt[state], cycleCounter
        seenAt[state] = cycleCounter


def solveDay() -> None:
    memoryBanks = np.array(list(map(int, getInput(6, 2017).strip().split('\t'))))
    firstSeen, secondSeen = redistributeTillRepeatState(memoryBanks)

    part1(secondSeen)
    part2(secondSeen - firstSeen)


solveDay()
