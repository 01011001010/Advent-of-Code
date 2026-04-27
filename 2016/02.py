from utils import getInput, part1, part2


deltas = {'L': (-1, 0),
          'R': (1, 0),
          'U': (0, -1),
          'D': (0, 1)}


def simulateBathroomAccessProcedure(buttonPresses: list[str],
                                    keyByPosition: dict[tuple[int, int], str],
                                    startPosition: tuple[int, int]) -> str:
    def move(position: tuple[int, int], movement: str,
             validPositions: set[tuple[int, int]]) -> tuple[int, int]:
        x, y = position
        dx, dy = deltas[movement]
        newPosition = (x + dx, y + dy)
        return newPosition if newPosition in validPositions else position

    validPositions = set(keyByPosition.keys())
    code = ""
    currentPosition = startPosition
    for movements in buttonPresses:
        for movement in movements:
            currentPosition = move(currentPosition, movement, validPositions)
        code += keyByPosition[currentPosition]

    return code


def solveDay() -> None:

    part1(simulateBathroomAccessProcedure(getInput(2, 2016).strip().splitlines(),
                                          {(c, r): number
                                           for r, row in enumerate("123 "
                                                                   "456 "
                                                                   "789".split())
                                           for c, number in enumerate(row)},
                                          (1, 1)))

    part2(simulateBathroomAccessProcedure(getInput(2, 2016).strip().splitlines(),
                                          {(c, r): key
                                           for r, row in enumerate("xx1xx "
                                                                   "x234x "
                                                                   "56789 "
                                                                   "xABCx "
                                                                   "xxDxx".split())
                                           for c, key in enumerate(row)
                                           if key != 'x'},
                                          (0, 2)))


solveDay()
