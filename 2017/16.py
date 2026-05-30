from utils import getInput, part1, part2
from collections import deque
import string


def spin(positions: deque, X: int) -> None:
    positions.rotate(X)


def exchange(positions: deque, A: int, B: int) -> None:
    positions[A], positions[B] = positions[B], positions[A]


def partner(positions: deque, A: int, B: int) -> None:
    exchange(positions, positions.index(A), positions.index(B))


def parse(danceMove, positions) -> None:
    if danceMove[0] == 's':
        spin(positions, int(danceMove[1:]))
    elif danceMove[0] == 'x':
        exchange(positions, *map(int, danceMove[1:].split('/')))
    elif danceMove[0] == 'p':
        partner(positions, *danceMove[1:].split('/'))


def solveDay() -> None:
    danceMoves = getInput(16, 2017).strip().split(',')
    positions = deque([ch for ch in string.ascii_lowercase[:16]])
    endPositions = ["".join(map(str, positions))]

    # Simulate dance until we see the starting order (loop found)
    while len(endPositions) == 1 or endPositions[-1] != endPositions[0]:
        for danceMove in danceMoves:
            parse(danceMove, positions)
        endPositions.append("".join(map(str, positions)))

    part1(endPositions[1])

    # Calculate where in the loop we end up
    part2(endPositions[1000000000 % (len(endPositions) - 1)])


solveDay()
