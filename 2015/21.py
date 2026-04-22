from utils import getInput, part1, part2, RememberMax, RememberMin
from itertools import combinations, product
from math import ceil
from re import sub, findall


class Gear:
    def __init__(self, name: str, cost: int, damage: int, armour: int) -> None:
        self._name = name
        self._cost = cost
        self._damage = damage
        self._armour = armour

    def __hash__(self) -> int:
        return self._name.__hash__()

    def getCost(self) -> int:
        return self._cost

    def getArmour(self) -> int:
        return self._armour

    def getDamage(self) -> int:
        return self._damage


def gearCombinations() -> set[tuple[Gear, ...]]:
    store = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""

    weapons, armour, rings = map(lambda block: [Gear(item,
                                                     int(cost),
                                                     int(damage),
                                                     int(defence))
                                                for item, cost, damage, defence
                                                in findall(r"(\w+\s?\+?\d?)\s+(\d+)\s+"
                                                           r"(\d+)\s+(\d+)", block)],
                                 sub(r"\w+:\s+Cost\s+Damage\s+Armor\s+", "",
                                     store).split("\n\n"))

    return set(map(lambda combination: tuple(set(combination[:2] + combination[2])),
                   product(weapons,
                           armour + [Gear("No armour", 0, 0, 0)],
                           combinations(rings + [Gear("No ring", 0, 0, 0),
                                                 Gear("No ring", 0, 0, 0)], 2))))


def simulateAndLogCost(gearCombination: tuple[Gear, ...], playerHP: int, enemyHP: int,
                       enemyDamage: int, enemyArmour: int, loseMemory: RememberMax,
                       winMemory: RememberMin) -> None:
    playerDamage = sum(map(Gear.getDamage, gearCombination))
    playerArmour = sum(map(Gear.getArmour, gearCombination))
    cost = sum(map(Gear.getCost, gearCombination))
    if (ceil(enemyHP / max(1, playerDamage - enemyArmour))
       <= ceil(playerHP / max(1, enemyDamage - playerArmour))):
        winMemory.newValueToConsider(cost)
    else:
        loseMemory.newValueToConsider(cost)


def solveDay() -> None:
    lose = RememberMax()
    win = RememberMin()
    for gear in gearCombinations():
        enemyHP, enemyDam, enemyArm = map(int, findall(r"\d+", getInput(21, 2015)))
        simulateAndLogCost(gear, 100, enemyHP, enemyDam, enemyArm, lose, win)

    part1(win.getValue())
    part2(lose.getValue())


solveDay()
