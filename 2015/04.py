from utils import getInput, part1, part2
from hashlib import md5


def findSuffix(secretKey: str, nZeros: int, start: int) -> int:
    suffix = start
    prefix = '0' * nZeros
    while md5((secretKey + str(suffix)).encode()).hexdigest()[:nZeros] != prefix:
        suffix += 1
    return suffix


def solveDay() -> None:
    secretKey = getInput(4, 2015).strip()
    fiveZeros = findSuffix(secretKey, 5, 0)
    part1(fiveZeros)
    part2(findSuffix(secretKey, 6, fiveZeros))


solveDay()
