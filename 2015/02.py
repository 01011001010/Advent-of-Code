from utils import getInput, part1, part2


def solveDay() -> None:
    gifts = map(lambda x: map(int, x.split('x')), getInput(2, 2015).strip().split())
    paper = 0
    ribbon = 0
    for length, width, height in gifts:
        longestSide = max((length, width, height))

        surface = 2 * (length * width + width * height + height * length)
        slack = length * width * height // longestSide
        paper += surface + slack

        around = 2 * (length + width + height - longestSide)
        bow = length * width * height
        ribbon += around + bow
    part1(paper)
    part2(ribbon)


solveDay()
