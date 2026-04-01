from utils import getInput, part1, part2
from operator import mul
from functools import reduce


def calculate(vals: list[int], op: str) -> int:
    # perform the summation or multiplication of the column (`vals`)
    return reduce(mul, vals, 1) if op == '*' else sum(vals)


def horizontalNotation(rawRows: list[str]) -> int:
    # extract the numbers and the operator for each column
    values = list(map(lambda line: list(map(int, line.split())), rawRows[:-1]))
    operators = rawRows[-1].split()

    # sum the evaluated columns
    return sum([calculate([row[column] for row in values], operators[column])
                for column in range(len(values[0]))])


def verticalNotation(rawRows: list[str]) -> int:
    grandTotal = 0

    # extract the leftmost vertical number
    values = [int(''.join([row[0] for row in rawRows[:-1] if row[0] != ' ']))]

    # find the first operator
    operator = rawRows[-1][0]

    # one by one traverse the character columns
    for column in range(1, len(rawRows[0])):
        if len({row[column] for row in rawRows}) == 1:
            # if the column contains only ' ', reduce the collected numbers
            grandTotal += calculate(values, operator)
            # clear the number collector
            values = []
        else:
            # parse the vertical number
            values.append(int(''.join([row[column]
                                       for row in rawRows[:-1]
                                       if row[column] != ' '])))
            # update operator, if contained in this column
            operator = rawRows[-1][column].strip() or operator

    # evaluate the last group (it has no blank column after to trigger it in the loop)
    grandTotal += calculate(values, operator)
    return grandTotal


def solveDay() -> None:
    rows = getInput(6, 2025).strip('\n').split('\n')

    part1(horizontalNotation(rows))
    part2(verticalNotation(rows))


solveDay()
