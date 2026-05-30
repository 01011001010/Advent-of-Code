from utils import getInput, part1, part2
from re import findall
from tqdm import tqdm
from typing import Iterator, Literal
from itertools import islice


def generator(AorB: Literal['A', 'B'], value: int, divisible: bool) -> Iterator[int]:
    multiplyBy = 16807 if AorB == 'A' else 48271
    checkDivisibility = 0b11 if AorB == 'A' else 0b111

    while True:
        value = (value * multiplyBy) % 2147483647

        if divisible and (value & checkDivisibility != 0):
            continue

        yield value


def checkMatch(a, b) -> bool:
    return (0b1111111111111111 & a) == (0b1111111111111111 & b)


def solveDay() -> None:
    a0, b0 = map(int, findall(r"\d+", getInput(15, 2017).strip()))

    part1(len(list(filter(lambda pair: checkMatch(*pair),
                          tqdm(islice(zip(generator('A', a0, False),
                                          generator('B', b0, False)),
                                      40000000),
                               total=40000000)))))
    part2(len(list(filter(lambda pair: checkMatch(*pair),
                          tqdm(islice(zip(generator('A', a0, True),
                                          generator('B', b0, True)),
                                      5000000),
                               total=5000000)))))


solveDay()
