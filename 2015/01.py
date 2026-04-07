from utils import getInput, part1, part2


def solveDay() -> None:
    instructions = getInput(1, 2015).strip()

    # For part 1, the order does not matter, just the frequencies
    part1(instructions .count('(') - instructions .count(')'))

    # For part 2, we just follow the instructions and see when we reach the basement
    currentFloor = 0
    for instructionPosition, instruction in enumerate(instructions, start=1):
        # enumerate with a shift, as we do not index from 0
        if instruction == '(':
            currentFloor += 1
            # No need to check if we reached the basement, the floors in the apartment
            # building are thankfully not on a loop XD
        else:
            currentFloor -= 1
            if currentFloor == -1:
                part2(instructionPosition)
                break


solveDay()
