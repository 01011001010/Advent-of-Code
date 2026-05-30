from utils import getInput, part1, part2


class Value:
    nowToInsert = 1

    def __init__(self, value: int, following: "None | Value" = None) -> None:
        self.value = value
        self.next = self if following is None else following

    def insertNext(self, value: int) -> None:
        self.next = Value(value, self.next)

    def stepAndInsert(self, steps: int) -> "Value":
        current = self
        for _ in range(steps):
            current = current.next
        current.insertNext(Value.nowToInsert)
        Value.nowToInsert += 1
        return current.next


def afterZero(stepSize: int, epochs: int) -> int:
    firstInsertPosition = firstInsertValue = isAfter0 = 1
    while True:
        lengthAfterFirstInsertPosition = firstInsertValue - firstInsertPosition
        firstInsertPosition = stepSize - (lengthAfterFirstInsertPosition % stepSize)
        firstInsertValue = firstInsertValue + ((lengthAfterFirstInsertPosition
                                                // stepSize) + 1)
        if firstInsertValue >= epochs:
            return isAfter0
        isAfter0 = firstInsertValue if firstInsertPosition == 1 else isAfter0


def solveDay() -> None:
    steps = int(getInput(17, 2017).strip())
    currentValue = Value(0)
    for _ in range(2017):
        currentValue = currentValue.stepAndInsert(steps)
    part1(currentValue.next.value)
    part2(afterZero(steps, 50000000))


solveDay()
