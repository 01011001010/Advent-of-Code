from utils import getInput, part1, part2
from typing import Iterable, Self


class Grid:
    class Light:
        def __init__(self, initialState: bool, alwaysOn: bool = False) -> None:
            self.state = initialState
            self.alwaysOn = alwaysOn
            self.currentlyLitNeighbours = 0
            self.neighbours = set()

        def isOn(self) -> bool:
            return self.state

        def countLitNeighbours(self) -> None:
            self.currentlyLitNeighbours = len([None
                                               for neighbour in self.neighbours
                                               if neighbour.isOn()])

        def advanceStage(self) -> None:
            self.state = (self.alwaysOn  # leave permanently lit lit
                          or self.currentlyLitNeighbours == 3
                          or (self.state and self.currentlyLitNeighbours == 2))

        def addNeighbours(self, newNeighbours: Iterable[Self]) -> None:
            self.neighbours.update(newNeighbours)

    def __init__(self, size: int, cornersAlwaysOn: bool = False) -> None:
        grid = {(column, row): self.Light(light == '#',
                                          (cornersAlwaysOn
                                           # ↓ check if corner position to leave lit
                                           and (row in (0, size-1)
                                                and column in (0, size-1))))
                for row, lightRow in enumerate(getInput(18, 2015).strip().splitlines())
                for column, light in enumerate(lightRow.strip())}

        for row, col in grid:
            grid[(row, col)].addNeighbours((grid[(row + dr, col + dc)]
                                            for dr, dc in ((-1, -1), (-1, 0), (-1, 1),
                                                           (0,  -1),          (0,  1),
                                                           (1,  -1), (1,  0), (1,  1))
                                            if (row + dr, col + dc) in grid))

        self.lights = set(grid.values())

    def advanceStage(self, numberOfROunds: int = 1) -> Self:
        if numberOfROunds < 1:
            raise ValueError("Cannot de-evolve the light-grid, provide a positive "
                             f"integer, not {numberOfROunds}.")
        for _ in range(numberOfROunds):
            # gather info for the stage advancement
            for light in self.lights:
                light.countLitNeighbours()

            # execute the change
            for light in self.lights:
                light.advanceStage()
        return self

    def countLitLights(self) -> int:
        return len([None for light in self.lights if light.isOn()])


def solveDay() -> None:
    part1(Grid(100).advanceStage(100).countLitLights())
    part2(Grid(100, True).advanceStage(100).countLitLights())


solveDay()
