from utils import getInput, part1, part2
from re import search


def solveDay() -> None:
    tickerTape = getInput(16, 2015).strip()
    part1((search(r"Sue (\d+): (("
                  r"(children: 3)|(cats: 7)|(samoyeds: 2)|(perfumes: 1)|(cars: 2)|"
                  r"(trees: 3)|(goldfish: 5)|(vizslas: 0)|(akitas: 0)|(pomeranians: 3)"
                  "),* *){3}", tickerTape)
           or ("", "Aunt Sue not found"))[1])
    part2((search(r"Sue (\d+): (("
                  r"(children: 3)|(cats: [89])|(samoyeds: 2)|(perfumes: 1)|(cars: 2)|"
                  r"(trees: [4-9])|(goldfish: [0-4])|(vizslas: 0)|(akitas: 0)|"
                  r"(pomeranians: [0-2])),* *){3}", tickerTape)
           or ("", "Aunt Sue not found"))[1])


solveDay()
