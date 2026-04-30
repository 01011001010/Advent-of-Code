from utils import getInput, part1, part2


def manhattanDistanceOfOfLocation(location: int) -> int:
    # Jump across the bend in the spiral without jumping over the location
    currentLocation = 1
    currentSide = 2
    while (nextLocation := currentLocation + currentSide // 2) < location:
        currentLocation = nextLocation
        currentSide += 1

    # Compute the Manhattan distance
    return ((currentSide + 1) // 4  # fully traversed side of the square
            + abs(currentSide // 4 - (location - currentLocation)))  # unfinished side


def assignLocation(x, y, memory) -> None:
    memory[(x, y)] = sum([memory.get((x + dx, y + dy), 0)
                          for dx in (-1, 0, 1)
                          for dy in (-1, 0, 1)])


def assignLocationsUntil(endIfOver: int) -> int:
    memory = {(0, 0): 1}
    x, y = (0, 0)
    dx, dy = (1, 0)
    while memory[(x, y)] <= endIfOver:
        if (x + dy, y - dx) not in memory:
            dx, dy = dy, -dx  # turn left

        x, y = x + dx, y + dy  # move

        assignLocation(x, y, memory)  # fill value

    return memory[(x, y)]


def solveDay() -> None:
    part1(manhattanDistanceOfOfLocation(int(getInput(3, 2017).strip())))
    part2(assignLocationsUntil(int(getInput(3, 2017).strip())))


solveDay()
