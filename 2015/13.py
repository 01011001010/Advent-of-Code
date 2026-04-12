from utils import getInput, part1, part2
from collections import defaultdict
from itertools import permutations
from re import split


def initHappinessMap() -> dict[tuple[str, str], int]:
    # Initialise potential happiness graph
    happinessMap = defaultdict(int)  # default/missing value = 0
    for seatingPair in getInput(13, 2015).strip().splitlines():
        guest1, val, guest2 = split(r"(?: would | happiness units by sitting next to )",
                                    (seatingPair.replace("gain ", '')
                                                .replace("lose ", '-')
                                                .strip('.')))

        # Undirected graph with total happiness per connection
        happinessMap[(guest1, guest2)] += int(val)
        happinessMap[(guest2, guest1)] += int(val)

    return happinessMap


def potentialHappiness(happinessMap: dict[tuple[str, str], int],
                       seatingPlan: tuple[str, ...]) -> int:
    # Translate seating arrangement to total happiness
    return sum(map(lambda pair: happinessMap[pair],
                   zip(seatingPlan, seatingPlan[1:] + (seatingPlan[0],))))


def findBestSeatingPlan(includeSelf: bool = False) -> int:
    happinessMap = initHappinessMap()
    maxPotentialHappiness = 0
    guests = (set(map(lambda pair: pair[0], happinessMap.keys())) |
              ({"Me"} if includeSelf else set()))
    rootGuest = next(iter(guests))  # Get a random guest as a fixed point at the table
    for seatingPlan in permutations(guests):
        if seatingPlan[0] != rootGuest:
            # Skip repeated arrangements (circular table)
            continue
        maxPotentialHappiness = max(maxPotentialHappiness,
                                    potentialHappiness(happinessMap, seatingPlan))
    return maxPotentialHappiness


def solveDay() -> None:
    part1(findBestSeatingPlan())
    part2(findBestSeatingPlan(True))


solveDay()
