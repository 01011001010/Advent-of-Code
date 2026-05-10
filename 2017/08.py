from utils import getInput, part1, part2, RememberMax


def solveDay() -> None:
    actions = {"inc": lambda a, b: a + b,
               "dec": lambda a, b: a - b}
    conditions = {">": lambda a, b: a > b,
                  "<": lambda a, b: a < b,
                  "==": lambda a, b: a == b,
                  ">=": lambda a, b: a >= b,
                  "<=": lambda a, b: a <= b,
                  "!=": lambda a, b: a != b}

    registers = {}
    allTimeMax = RememberMax()
    for instruction in getInput(8, 2017).strip().splitlines():
        register, action, value, _, *conditionDetails = instruction.split(" ")
        conditionRegister, condition, conditionValue = conditionDetails
        if conditions[condition](registers.get(conditionRegister, 0),
                                 int(conditionValue)):
            registers[register] = actions[action](registers.get(register, 0),
                                                  int(value))
            allTimeMax.newValueToConsider(registers[register])

    part1(max(registers.values()))
    part2(allTimeMax.getValue())


solveDay()
