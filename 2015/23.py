from utils import getInput, part1, part2
from typing import Callable


def half(registers: dict[str, int], instructionIndex: int, register: str) -> int:
    registers[register] //= 2
    return instructionIndex + 1


def triple(registers: dict[str, int], instructionIndex: int, register: str) -> int:
    registers[register] *= 3
    return instructionIndex + 1


def increase(registers: dict[str, int], instructionIndex: int, register: str) -> int:
    registers[register] += 1
    return instructionIndex + 1


def jump(registers: dict[str, int], instructionIndex: int, offset: str) -> int:
    return instructionIndex + int(offset)


def jumpIfEven(registers: dict[str, int], instructionIndex: int, register: str,
               offset: str) -> int:
    if (registers[register] & 1) == 0:
        return instructionIndex + int(offset)
    return instructionIndex + 1


def jumpIfOne(registers: dict[str, int], instructionIndex: int, register: str,
              offset: str) -> int:
    if registers[register] == 1:
        return instructionIndex + int(offset)
    return instructionIndex + 1


def parseLineToFunction(instructionLine: str) -> Callable:
    operation, *args = instructionLine.split(' ')

    operations = {"hlf": half,
                  "tpl": triple,
                  "inc": increase,
                  "jmp": jump,
                  "jie": jumpIfEven,
                  "jio": jumpIfOne}
    return lambda registers, idx: operations[operation](registers, idx, *args)


def simulate(a: int, programme: list[Callable]) -> int:
    currentPosition = 0
    registers = {'a': a, 'b': 0}
    while currentPosition < len(programme):
        currentPosition = programme[currentPosition](registers, currentPosition)

    return registers['b']


def solveDay() -> None:
    programme = list(map(lambda line: parseLineToFunction(line.replace(',', "")),
                     getInput(23, 2015).strip().split('\n')))
    part1(simulate(0, programme))
    part2(simulate(1, programme))


solveDay()
