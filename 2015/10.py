from utils import getInput, part1, part2


# The first solution was simple simulation of the game and the spoken sequences. It ran
# decently quick. Nonetheless, I looked into writing a more clever solution. I came to
# realise that the sequence will only consist of the characters '1', '2', '3' and never
# '4' or higher (proof hint: to produce the first number 4+, you have to have one of the
# a sequences '1111...', '2222...', '3333...', which will never happen. The rest of the
# proof is left to the reader.) This lead me on a path of trying to compress the
# sequence. I, however, emerged empty-handed, as the nature of the short sequences of 3
# possible characters does not offer nice compact notation (the same reason, why the
# sequence lengths increase between rounds). Another idea was to create a dictionary of
# how subsequences evolve in a number of rounds. The issue with this approach was the
# fact that the syntax tree is not actually a tree, as after one round, the edges of the
# sequences generated from a subsequence do in fact interact, and thus the deterministic
# section of the descendant sequence gets smaller with each generation. The speed of the
# trivial approach of simply creating the sequence warrants no need to look for other
# unnecessarily complicated solutions.

def lookAndSay(sequence: str) -> str:
    spokenSequence = ""
    lastSeen = sequence[0]
    n = 1
    for nowSeeing in sequence[1:] + 'X':  # X to force speech of the last number
        if nowSeeing == lastSeen:
            n += 1
        else:
            spokenSequence += str(n) + lastSeen
            lastSeen = nowSeeing
            n = 1
    return spokenSequence


def playRounds(sequence: str, nRounds: int) -> str:
    if nRounds == 0:
        return sequence
    return lookAndSay(playRounds(sequence, nRounds - 1))


def solveDay() -> None:
    sequence = playRounds(getInput(10, 2015).strip(), 40)
    part1(len(sequence))
    part2(len(playRounds(sequence, 10)))


solveDay()
