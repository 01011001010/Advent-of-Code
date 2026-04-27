from utils import getInput, part1, part2


def manhattanDistanceFromOrigin(x, y) -> int:
    return abs(x) + abs(y)


class Path:
    class LineSegment:
        multiplierTable = {'E': (1, 0),
                           'W': (-1, 0),
                           'S': (0, -1),
                           'N': (0, 1)}
        turnTable = {('N', 'R'): 'E',
                     ('N', 'L'): 'W',
                     ('E', 'R'): 'S',
                     ('E', 'L'): 'N',
                     ('S', 'R'): 'W',
                     ('S', 'L'): 'E',
                     ('W', 'R'): 'N',
                     ('W', 'L'): 'S'}

        def __init__(self, x: int, y: int, facing: str, turn: str,
                     distance: int) -> None:
            self.facingAfter = Path.LineSegment.turnTable[(facing, turn)]
            self.vertical = self.facingAfter in "SN"
            mx, my = Path.LineSegment.multiplierTable[self.facingAfter]
            self.x = (x, x + mx * distance)
            self.y = (y, y + my * distance)
            self.x1 = min(self.x)
            self.y1 = min(self.y)
            self.x2 = max(self.x)
            self.y2 = max(self.y)

        def nextLine(self, turn: str, distance: int) -> "Path.LineSegment":
            return Path.LineSegment(self.x[1], self.y[1], self.facingAfter, turn,
                                    distance)

        def overlaps(self, other: "Path.LineSegment") -> bool:
            if self.vertical:
                if other.vertical:
                    return (self.x1 == other.x1 and self.y1 <= other.y2
                            and other.y1 <= self.y2)
                return (self.y1 <= other.y1 <= self.y2
                        and other.x1 <= self.x1 <= other.x2)
            if other.vertical:
                return (self.x1 <= other.x1 <= self.x2
                        and other.y1 <= self.y1 <= other.y2)
            return self.y1 == other.y1 and self.x1 <= other.x2 and other.x1 <= self.x2

        def pointOfOverlap(self, other: "Path.LineSegment") -> tuple[int, int]:
            if self.overlaps(other):
                if self.vertical != other.vertical:
                    return sorted(self.x + other.x)[1], sorted(self.y + other.y)[1]
                raise NotImplementedError("My solution crossed at 90° angle ;-; .")
            raise ValueError("Line segments do not overlap.")

        def endOfSegment(self) -> tuple[int, int]:
            return self.x[1], self.y[1]

    def __init__(self, directions: list[str]) -> None:
        (turn, *distance), *instructions = directions
        self.lineSegments = [Path.LineSegment(0, 0, 'N', turn, int(''.join(distance)))]
        self.revisitedPlace = None
        for (turn, *distance) in instructions:
            self.lineSegments.append((self.lineSegments[-1]
                                          .nextLine(turn, int(''.join(distance)))))
            for olderLineSegment in self.lineSegments[:-3]:
                if (self.revisitedPlace is None
                   and olderLineSegment.overlaps(endSoFar := self.lineSegments[-1])):
                    self.revisitedPlace = olderLineSegment.pointOfOverlap(endSoFar)

    def distanceToTheEndOfPath(self) -> int:
        return manhattanDistanceFromOrigin(*self.lineSegments[-1].endOfSegment())

    def distanceToFirstRepeatVisit(self) -> int:
        if self.revisitedPlace is None:
            raise ValueError("No place was visited twice.")
        return manhattanDistanceFromOrigin(*self.revisitedPlace)


def solveDay() -> None:
    path = Path(getInput(1, 2016).strip().split(", "))

    part1(path.distanceToTheEndOfPath())
    part2(path.distanceToFirstRepeatVisit())


solveDay()
