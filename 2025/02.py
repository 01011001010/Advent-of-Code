from utils import getInput, part1, part2


def repeatedInRange(start: int, end: int, repeatLength: int = -1) -> set[int]:
    # Calculate string lengths
    lenStart = len(str(start))
    lenEnd = len(str(end))

    # Dynamic repeat length (part 1)
    if repeatLength == -1:
        # Cut off range start/end for numbers with odd length as these will never
        # contain invalid IDs
        if lenStart != lenEnd:
            if lenStart % 2 == 1:
                start = 10 ** lenStart
                lenStart = len(str(start))
            elif lenEnd % 2 == 1:
                end = 10 ** (lenEnd - 1) - 1
                lenEnd = len(str(end))
        # No invalid IDs due to odd number length
        if lenStart % repeatLength != 0 or lenStart == 3:
            return set()

        # Set dynamic repeat length
        repeatLength = lenStart // 2

    timesRepeated = lenStart // repeatLength
    if lenStart != lenEnd:
        raise ValueError("Split ranges spanning multiple magnitudes for separate "
                         "processing")
    # Trivial solution with mismatched repeat length
    if lenStart % repeatLength != 0:
        return set()

    # Exclude repeated numbers from if out of range
    # Example:
    #   1155, first to consider should be 1212, not 1111
    left = int(str(start)[:repeatLength])
    if int(str(left) * timesRepeated) < start:
        left += 1
    # Example:
    #   5511, last to consider should be 5454, not 5555
    right = int(str(end)[:repeatLength])
    if int(str(right) * timesRepeated) > end:
        right -= 1

    # Generate all invalid IDs
    return set(int(str(num) * timesRepeated) for num in range(left, right + 1))


def sumInvalidVariableLength(start: int, end: int) -> int:
    lenStart = len(str(start))
    lenEnd = len(str(end))
    if lenStart != lenEnd:
        if abs(lenStart - lenEnd) != 1:
            raise NotImplementedError("Puzzle expected to not contain ranges spanning "
                                      "more than 2 magnitudes")
        # Split the range
        return (sumInvalid(start, 10 ** (lenEnd - 1) - 1) +
                sumInvalid(10 ** lenStart, end))
    return sumInvalid(start, end)


def sumInvalid(start: int, end: int) -> int:
    lenStart = len(str(start))
    if lenStart != len(str(end)):
        raise ValueError("Split ranges spanning multiple magnitudes for separate "
                         "processing")
    # Generate and sum all invalid IDs with arbitrary repeatLength
    return sum(set().union(*(repeatedInRange(start, end, n)
                             for n in range(1, 6)
                             if lenStart % n == 0 and lenStart // n > 1)))


def solveDay() -> None:
    ranges = getInput(2, 2025).strip().split(',')
    part1(sum(set().union(*(repeatedInRange(*map(int, r.split('-')))
                            for r in ranges))))
    part2(sum(sumInvalidVariableLength(*map(int, r.split('-')))
              for r in ranges))


solveDay()
