from utils import getInput, part1, part2
import json
from typing import Any


def sumNumbers(datum: Any) -> tuple[int, int]:
    # parse deeper until numbers found
    # keep track of which objects are excluded as they contain the string "red"
    # first returned  number is just the simple sum, the second is "non-red" sum
    if isinstance(datum, int):
        return datum, datum
    if isinstance(datum, (list, tuple)):
        processed = tuple(map(sumNumbers, datum))
        return sum(n for n, _ in processed), sum(n for _, n in processed)
    if isinstance(datum, dict):
        processed = tuple(map(sumNumbers, datum.items()))
        return (sum(n for n, _ in processed),
                sum(n for _, n in processed) if "red" not in datum.values() else 0)
    return 0, 0


def solveDay() -> None:
    data = json.loads(getInput(12, 2015))
    sumAll, sumNonRed = sumNumbers(data)
    part1(sumAll)
    part2(sumNonRed)


solveDay()
