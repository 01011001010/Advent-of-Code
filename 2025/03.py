from utils import getInput, part1, part2


def maxJoltage(bank: str, nBatteries: int = 2) -> int:
    # separate last `nBatteries` digits to prevent running out
    suffixes: list[str] = list(reversed(list(bank[-nBatteries:])))
    prefix = bank[:-nBatteries]

    # greedily build the max joltage
    joltage = ""
    while suffixes:
        # select the first occurrence of the highest contained digit
        # with the prefix and `suffixes.pop` we are disallowing selection out of order
        # or running out of digits
        pref = findDigit(prefix + suffixes.pop())
        joltage += pref[0]
        prefix = pref[1:]
    return int(joltage)


def findDigit(subbank: str) -> str:
    # find the first occurrence of the highest digit and cut off the battery bank before
    index = subbank.find(max(subbank))
    return subbank[index:]


def solveDay() -> None:
    batteryBanks = getInput(3, 2025).strip().split()

    # find max joltage per battery bank and sum them
    part1(sum(map(lambda bank: maxJoltage(bank, 2), batteryBanks)))
    part2(sum(map(lambda bank: maxJoltage(bank, 12), batteryBanks)))


solveDay()
