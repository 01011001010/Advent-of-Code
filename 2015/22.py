from utils import getInput, part1, part2
from heapq import heappop, heappush
from re import findall


class MatchState:
    def __init__(self, mageHP: int, bossHP: int, manaAvailable: int, manaSpent: int,
                 bossDamage: int, hardMode: bool, effectTTLs: dict[str, int],
                 bossKilled: bool) -> None:
        self.mageHP = mageHP
        self.bossHP = bossHP
        self.manaAvailable = manaAvailable
        self.manaSpent = manaSpent
        self.bossDamage = bossDamage
        self.hardMode = hardMode
        self.effectTTLs = effectTTLs
        self.bossKilled = bossKilled
        self.spells = {"Magic Missile": (53, 4, 0, lambda effects: None),
                       "Drain": (73, 2, 2, lambda effects: None),
                       "Shield": (113, 0, 0,
                                  lambda effects: effects.update({"Shield": 6})),
                       "Poison": (173, 0, 0,
                                  lambda effects: effects.update({"Poison": 6})),
                       "Recharge": (229, 0, 0,
                                    lambda effects: effects.update({"Recharge": 5}))}

    def copyState(self) -> "MatchState":
        return MatchState(self.mageHP, self.bossHP, self.manaAvailable, self.manaSpent,
                          self.bossDamage, self.hardMode, self.effectTTLs.copy(),
                          self.bossKilled)

    def enactEffects(self) -> None:
        for effect in list(self.effectTTLs.keys()):
            if self.effectTTLs[effect] == 0:
                del self.effectTTLs[effect]
                continue
            else:
                self.effectTTLs[effect] -= 1
            if effect == "Poison":
                self.bossHP -= 3
                if self.bossHP < 1:
                    self.bossKilled = True
            elif effect == "Recharge":
                self.manaAvailable += 101

    def bossAttack(self) -> None:
        self.mageHP -= (max(1, self.bossDamage - 7)
                        if "Shield" in self.effectTTLs
                        else self.bossDamage)

    def mageSpell(self, spell: str) -> bool:
        manaCost, damage, healing, effectFunction = self.spells[spell]
        if (self.manaAvailable < manaCost  # not enough mana
           or self.effectTTLs.get(spell, 0) > 0):  # effect already active
            return False
        self.manaSpent += manaCost
        self.manaAvailable -= manaCost
        self.bossHP -= damage
        self.mageHP += healing
        effectFunction(self.effectTTLs)
        return True

    def allPossibleNextStates(self) -> list["MatchState"]:
        # Mage turn start
        if self.hardMode:
            self.mageHP -= 1
            if self.mageHP < 1:
                return []  # Mage dies before casting any spell

        self.enactEffects()
        if self.bossKilled:
            return [self]  # Boss killed by poison effect before Mage's turn

        states = []
        for spell in self.spells:
            newState = self.copyState()
            if not newState.mageSpell(spell):
                continue  # spell not castable

            # Boss turn start
            newState.enactEffects()

            if newState.bossHP < 1:
                newState.bossKilled = True  # Boss killed by a spell or poison effect
            else:
                newState.bossAttack()
                if newState.mageHP < 1:
                    continue  # Mage killed by boss' attack

            states.append(newState)
        return states

    def __lt__(self, other: "MatchState") -> bool:
        # for heap ordering
        if self.manaSpent == other.manaSpent:
            return self.bossKilled
        return self.manaSpent < other.manaSpent


def findCheapest(heardMode: bool, bossHP: int, bossDamage: int) -> int:
    states = [MatchState(50, bossHP, 500, 0, bossDamage, heardMode, {}, False)]
    while states:
        matchState = heappop(states)
        if matchState.bossKilled:
            # heap ordering guarantees, that the first win scenario is the cheapest
            return matchState.manaSpent
        for nextState in matchState.allPossibleNextStates():
            heappush(states, nextState)
    return -1


def solveDay() -> None:
    bossHP, bossDamage = map(int, findall(r"\d+", getInput(22, 2015)))

    part1(findCheapest(False, bossHP, bossDamage))
    part2(findCheapest(True, bossHP, bossDamage))


solveDay()
