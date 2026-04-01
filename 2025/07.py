from utils import getInput, part1, part2


def solveDay() -> None:
    rows = getInput(7, 2025).strip().split()

    split = 0  # split counter
    beams = {rows[0].index('S'): 1}  # one starting beam

    # The beam travels only downwards, allowing us to solve each level in order
    for row in rows[1:]:
        for col, char in enumerate(row):
            if char == '^' and col in beams:
                # when a beam hits a splitter, it splits to the left and right
                # instead of following 10^13 individual beams, for each x position, we
                # track the beam count at once, as it behaves the same

                # of note is also, that while we probably should separate the beam
                # description dictionary for each row, a look into the puzzle input
                # reveals that no 2 splitters are right next to each other, so a beam
                # that we just split will not be split again on the same level
                beams[col-1] = beams.get(col-1, 0) + beams[col]
                beams[col+1] = beams.get(col+1, 0) + beams.pop(col)

                # for part 1, we just track the number of splitters hit by a beam
                split += 1

    part1(split)
    # for part 2, we sum the beam counts at the end
    part2(sum(beams.values()))


solveDay()
