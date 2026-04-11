from utils import getInput, part1, part2
from re import findall


def escapeBloat(string: str) -> int:
    matches = list(map(lambda x: max(map(len, x)),
                       findall(r'(\\")|(\\\\)|(\\x[0-f]{2})', string)))
    # each match group represents one character
    return sum(matches) - len(matches) + 2  # +2 for the encapsulating ""


def additionalEscapeBloat(string: str) -> int:
    # return len(findall(r'[\\"]', string)) + 2
    return string.count('\\') + string.count('\"') + 2  # +2 for the encapsulating ""


def solveDay() -> None:
    strings = getInput(8, 2015).strip().splitlines()
    part1(sum((escapeBloat(string.strip()) for string in strings)))
    part2(sum((additionalEscapeBloat(string.strip()) for string in strings)))


solveDay()
