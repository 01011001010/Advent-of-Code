from utils import getInput, part1, part2
from math import lcm
from itertools import combinations


def solveDay() -> None:
    spreadsheetData = list(map(lambda row: list(map(int, row.split('\t'))),
                               getInput(2, 2017).strip().split('\n')))
    part1(sum(map(lambda row: max(row) - min(row),
                  spreadsheetData)))
    part2(sum(map(lambda row: sum(map(lambda pair: (max(pair) // min(pair)),
                                      filter(lambda pair: lcm(*pair) == max(pair),
                                             combinations(row, 2)))),
                  spreadsheetData)))


solveDay()
