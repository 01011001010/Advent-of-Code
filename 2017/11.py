from utils import getInput, part1, part2, RememberMax


class Child:
    def __init__(self) -> None:
        self.column = 0
        self.row = 0
        self.distanceAway = 0
        self.pathTraced = False
        self.furthestAway = RememberMax()
        self.currentSextant = "centre"

    def updatePosition(self, direction: str) -> None:
        deltaCol, deltaRow = {'n': (0, 2),
                              's': (0, -2),
                              "nw": (-1, 1),
                              "ne": (1, 1),
                              "sw": (-1, -1),
                              "se": (1, -1)}[direction]
        self.column += deltaCol
        self.row += deltaRow

    def checkIfOnADiagonal(self) -> None:
        if self.column == 0 and self.row == 0:
            self.currentSextant = "centre"
        elif self.column == 0 and self.row > 0:
            self.currentSextant = "northDiagonal"
        elif self.column == 0 and self.row < 0:
            self.currentSextant = "southDiagonal"
        elif self.column == self.row and self.column > 0:
            self.currentSextant = "northEastDiagonal"
        elif self.column == - self.row and self.column > 0:
            self.currentSextant = "southEastDiagonal"
        elif self.column == self.row and self.column < 0:
            self.currentSextant = "southWestDiagonal"
        elif self.column == - self.row and self.column < 0:
            self.currentSextant = "northWestDiagonal"

    def sextantChangeMapping(self) -> dict[str, str]:
        return {"centre": {'n': "northDiagonal",
                           's': "southDiagonal",
                           "nw": "northWestDiagonal",
                           "ne": "northEastDiagonal",
                           "sw": "southWestDiagonal",
                           "se": "southEastDiagonal"},
                "northDiagonal": {"nw": "nw",
                                  "ne": "ne",
                                  "sw": "nw",
                                  "se": "ne"},
                "southDiagonal": {"nw": "sw",
                                  "ne": "se",
                                  "sw": "sw",
                                  "se": "se"},
                "northEastDiagonal": {'n': "ne",
                                      's': "e",
                                      "nw": "ne",
                                      "se": "e"},
                "southEastDiagonal": {'n': "e",
                                      's': "se",
                                      "ne": "e",
                                      "sw": "se"},
                "southWestDiagonal": {'n': "w",
                                      's': "sw",
                                      "nw": "w",
                                      "se": "sw"},
                "northWestDiagonal": {'n': "nw",
                                      's': "w",
                                      "ne": "nw",
                                      "sw": "w"}
                }.get(self.currentSextant, {})

    def distanceChangeMapping(self) -> dict[str, int]:
        return {"centre": {},
                "northDiagonal": {'nw': 1, 'n': 1, 'ne': 1,
                                  'sw': 0, 'se': 0,
                                  's': -1},
                "southDiagonal": {'sw': 1, 's': 1, 'se': 1,
                                  'nw': 0, 'ne': 0,
                                  'n': -1},
                "northEastDiagonal": {'n': 1, 'ne': 1, 'se': 1,
                                      's': 0, 'nw': 0,
                                      'sw': -1},
                "southEastDiagonal": {'s': 1, 'se': 1, 'ne': 1,
                                      'n': 0, 'sw': 0,
                                      'nw': -1},
                "southWestDiagonal": {'s': 1, 'sw': 1, 'nw': 1,
                                      'n': 0, 'se': 0,
                                      'ne': -1},
                "northWestDiagonal": {'n': 1, 'nw': 1, 'sw': 1,
                                      's': 0, 'ne': 0,
                                      'se': -1},
                'e': {'ne': 1, 'se': 1,
                      'n': 0, 's': 0,
                      'nw': -1, 'sw': -1},
                'se': {'se': 1, 's': 1,
                       'ne': 0, 'sw': 0,
                       'n': -1, 'nw': -1},
                'sw': {'sw': 1, 's': 1,
                       'nw': 0, 'se': 0,
                       'n': -1, 'ne': -1},
                'w': {'nw': 1, 'sw': 1,
                      'n': 0, 's': 0,
                      'ne': -1, 'se': -1},
                'nw': {'nw': 1, 'n': 1,
                       'sw': 0, 'ne': 0,
                       's': -1, 'se': -1},
                'ne': {'ne': 1, 'n': 1,
                       'se': 0, 'nw': 0,
                       's': -1, 'sw': -1},
                }.get(self.currentSextant, {})

    def oneStep(self, step: str) -> None:
        self.checkIfOnADiagonal()
        self.distanceAway += self.distanceChangeMapping().get(step, 1)
        self.currentSextant = self.sextantChangeMapping().get(step, self.currentSextant)
        self.updatePosition(step)
        self.furthestAway.newValueToConsider(self.distanceAway)

    def seeWhereThePathLeads(self) -> int:
        self.pathTraced = True
        for step in getInput(11, 2017).strip().split(','):
            self.oneStep(step)
        return self.distanceAway

    def furthestAwayAlongThePath(self) -> int:
        if not self.pathTraced:
            raise ValueError("Simulate the path first (use .seeWhereThePathLeads())")
        return self.furthestAway.getValue()


def solveDay() -> None:
    child = Child()

    part1(child.seeWhereThePathLeads())
    part2(child.furthestAwayAlongThePath())


solveDay()
