from utils import getInput, part1, part2


def visitedAtLeastOnce(instructions: str) -> set[tuple[int, int]]:
    x = y = 0
    visited = {(0, 0)}
    deltas = [{'<': (-1, 0),
               '>': (1,  0),
               '^': (0, -1),
               'v': (0,  1)}[instruction] for instruction in instructions]
    for dx, dy in deltas:
        x += dx
        y += dy
        visited.add((x, y))
    return visited


def solveDay() -> None:
    instructions = getInput(3, 2015).strip()
    part1(len(visitedAtLeastOnce(instructions)))
    part2(len(visitedAtLeastOnce(instructions[::2]) |
              visitedAtLeastOnce(instructions[1::2])))


solveDay()
