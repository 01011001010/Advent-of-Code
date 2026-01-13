import requests as requests
from pathlib import Path
from datetime import date
from collections.abc import Callable


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
    with open(Path(__file__).parent.parent / "sessionCookie.txt", 'r') as cookieFile:
        cookies = {"session": cookieFile.readline().strip()}
    response = requests.get(url=url, cookies=cookies)
    if not response.ok:
        raise Exception("Unexpected response from server during puzzle input fetch")
    return response.text


def _part(i: int, answer: int | str):
    print(f'Part {i}: {answer}')


def part1(answer: int | str = ''):
    _part(1, answer)


def part2(answer: int | str = ''):
    _part(2, answer)
