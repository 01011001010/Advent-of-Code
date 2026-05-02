from utils import getInput, part1, part2


def containsNoDuplicates(passphrase: str) -> bool:
    return len(set(passphrase.split(' '))) > passphrase.count(' ')


def containsNoAnagrams(passphrase: str) -> bool:
    return len(set(map(lambda word: "".join(sorted(word)),
                       passphrase.split(' ')))
               ) > passphrase.count(' ')


def solveDay() -> None:
    passphrases = getInput(4, 2017).strip().splitlines()
    part1(len(valid := list(filter(containsNoDuplicates, passphrases))))
    part2(len(list(filter(containsNoAnagrams, valid))))


solveDay()
