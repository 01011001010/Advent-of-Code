from utils import getInput, part1, part2


def isNice(word: str) -> bool:
    if not word:  # empty string
        return False
    vowels = "aeiou".count(word[0])  # count the first character
    doubleChar = False
    naughtyBigrams = set(map(tuple, ("ab", "cd", "pq", "xy")))
    for bigram in zip(word, word[1:]):
        if bigram in naughtyBigrams:
            return False
        if bigram[1] in "aeiou":  # count from the second character
            vowels += 1
        if bigram[0] == bigram[1]:
            doubleChar = True
    return doubleChar and vowels > 2


def isNiceImproved(word: str) -> bool:
    if not word:  # empty string
        return False
    doubleCharHugging = False
    repeatedBigram = False
    bigramPositions = {tuple(word[:2]): 0}  # log the first bigram
    for position, trigram in enumerate(zip(word, word[1:], word[2:]), start=1):
        if not repeatedBigram:  # one is enough
            if (bigram := trigram[1:]) not in bigramPositions:
                # if seen for the first time, log the position
                bigramPositions[bigram] = position
            elif (position - bigramPositions[bigram]) != 1:
                # if already seen, check if not overlapping
                repeatedBigram = True

        if not doubleCharHugging and trigram[0] == trigram[2]:
            doubleCharHugging = True
        if doubleCharHugging and repeatedBigram:
            return True
    return False


def solveDay() -> None:
    SantasTextFile = getInput(5, 2015).strip().split()

    part1(sum([isNice(word) for word in SantasTextFile]))
    part2(sum([isNiceImproved(word) for word in SantasTextFile]))  # ... nice


solveDay()
