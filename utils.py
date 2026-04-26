import requests as requests
from pathlib import Path
from datetime import date
from collections.abc import Callable
from typing import Any


_loadedInput = {}


def _memoizeInput(loadFunction: Callable[[int, int], str]) -> Callable[[int, int], str]:
    def _answerLoadingRequest(day: int, year: int):
        if (date := (day, year)) not in _loadedInput:
            _loadedInput[date] = loadFunction(*date)
        return _loadedInput[date]
    return _answerLoadingRequest


@_memoizeInput
def getInput(day: int, year: int = date.today().year) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    with open(Path(__file__).resolve().parent / "sessionCookie.txt", 'r') as cookieFile:
        cookies = {"session": cookieFile.readline().strip()}
    response = requests.get(url=url, cookies=cookies)
    if not response.ok:
        raise Exception("Unexpected response from server during puzzle input fetch")
    return response.text


def _part(i: int, answer: int | str) -> None:
    print(f'Part {i}: {answer}')


def part1(answer: int | str = '') -> None:
    _part(1, answer)


def part2(answer: int | str = '') -> None:
    _part(2, answer)


def bothParts(answer1: int | str = '', answer2: int | str = '') -> None:
    _part(1, answer1)
    _part(2, answer2)


class RememberExtreme:
    def __init__(self) -> None:
        self.value = None
        self.defaultStr = None

    def __str__(self) -> str:
        if self.value is None:
            if self.defaultStr is None:
                raise NotImplementedError("Do not use RememberExtreme class directly")
            return self.defaultStr
        return str(self.value)

    def getValue(self) -> int:
        if self.value is None:
            raise ValueError("No values to choose from")
        return self.value

    def newValueToConsider(self, value: Any) -> None:
        raise NotImplementedError("Do not use RememberExtreme class directly")


class RememberMax(RememberExtreme):
    def __init__(self) -> None:
        self.value = None
        self.defaultStr = "Minus infinity"

    def newValueToConsider(self, value: int) -> None:
        if self.value is None or self.value < value:
            self.value = value


class RememberMin(RememberExtreme):
    def __init__(self) -> None:
        self.value = None
        self.defaultStr = "Infinity"

    def newValueToConsider(self, value: int) -> None:
        if self.value is None or self.value > value:
            self.value = value
