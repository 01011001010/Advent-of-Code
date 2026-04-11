from utils import getInput, part1, part2
import numpy as np
import re


def simulate(instructions: list[str], brightness: bool = False) -> int:
    # we are simply simulating the lights
    # numpy for ease of indexing and speed
    grid = np.full((1000, 1000), 0 if brightness else False)
    for instructionLine in instructions:
        if m := re.search(r"(.+) (\d+),(\d+) through (\d+),(\d+)", instructionLine):
            instruction, *coordinates = m.groups()
            c1, r1, c2, r2 = map(int, coordinates)
            c2, r2 = c2 + 1, r2 + 1

            if brightness:
                if instruction == "toggle":
                    grid[r1:r2, c1:c2] += 2
                elif instruction == "turn on":
                    grid[r1:r2, c1:c2] += 1
                else:
                    grid[r1:r2, c1:c2] -= 1
                    grid[grid < 0] = 0
            else:
                if instruction == "toggle":
                    grid[r1:r2, c1:c2] = np.logical_not(grid[r1:r2, c1:c2])
                elif instruction == "turn on":
                    grid[r1:r2, c1:c2] = True
                else:
                    grid[r1:r2, c1:c2] = False

    return grid.sum()


def solveDay() -> None:
    instructions = getInput(6, 2015).strip().splitlines()

    part1(simulate(instructions))
    part2(simulate(instructions, True))


solveDay()
