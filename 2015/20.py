from utils import getInput, part1, part2
import numpy as np


def robinsInequality(n: int) -> int:
    # see https://en.wikipedia.org/wiki/Divisor_function#Growth_rate
    return np.exp(np.euler_gamma) * n * np.log(np.log(n))


def findLowerBoundForHouseNumber(numberOfPresents: int,
                                 presentsPerHouse: int,
                                 lower: int | None = None,
                                 upper: int | None = None) -> int:
    upper = (numberOfPresents // presentsPerHouse) if upper is None else upper
    lower = 0 if lower is None else lower

    if upper - lower < 100:  # Not worth it finding a precise value
        return lower

    mid = (upper + lower) // 2
    upperBoundAtMid = robinsInequality(mid) * presentsPerHouse

    if upperBoundAtMid > numberOfPresents:
        return findLowerBoundForHouseNumber(numberOfPresents, presentsPerHouse,
                                            lower, mid)
    return findLowerBoundForHouseNumber(numberOfPresents, presentsPerHouse, mid, upper)


def solveDay() -> None:
    # Literals from the puzzle text
    giftsPerHouse = 10
    giftsPerHouseLazy = 11
    housesPerElfLazy = 50

    giftsNeeded = int(getInput(20, 2015).strip())

    # Find the lower bound for the house number using an upper bound for the divisor
    # function
    lowerBound = findLowerBoundForHouseNumber(giftsNeeded, giftsPerHouse)
    upperBound = giftsNeeded // giftsPerHouse

    # Simulate elves delivering presents ignoring houses below the lower bound
    houses = np.zeros(upperBound - lowerBound)
    housesLazy = np.zeros(upperBound - lowerBound)

    for elf in range(1, upperBound):
        # Mind the shift where the 0th house is the `lower bound`th
        firstVisitedWithinBounds = (elf - lowerBound) % elf
        houses[firstVisitedWithinBounds::elf] += giftsPerHouse * elf

        if (elf+1)*housesPerElfLazy >= lowerBound:  # Avoid negative indexing misbehave
            housesLazy[firstVisitedWithinBounds:
                       (elf + 1) * housesPerElfLazy - lowerBound:
                       elf] += giftsPerHouseLazy * elf

        # We can end when the any house visited first by some elf received enough gifts
        if (elf > lowerBound and (houses[elf - lowerBound] >= giftsNeeded and
                                  housesLazy[elf - lowerBound] >= giftsNeeded)):
            break

    part1((np.nonzero(houses >= giftsNeeded)[0][0]) + lowerBound)
    part2((np.nonzero(housesLazy >= giftsNeeded)[0][0]) + lowerBound)


solveDay()
