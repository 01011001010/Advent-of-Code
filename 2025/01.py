from utils import getInput, part1, part2


def rotate(position, endAtZero, passZero, instruction) -> tuple[int, int, int]:
    # input line parsing
    direction = instruction[0]
    steps = int(instruction[1:])

    # full-circle rotations
    passZero += steps // 100
    steps %= 100

    # partial rotation
    position += steps * {'R': 1, 'L': -1}[direction]
    if position > 99:
        passZero += 1
    if position <= 0:
        passZero += 1 if -position != steps else 0  # excluding move from position 0

    # position after all rotations
    position %= 100
    if position == 0:
        endAtZero += 1

    return position, endAtZero, passZero


def solveDay() -> None:
    state = (50, 0, 0)  # position, count of stops at 0, count of 0 passes
    for line in getInput(1, 2025).strip().split():
        state = rotate(*state, line)

    part1(state[1])
    part2(state[2])


solveDay()
