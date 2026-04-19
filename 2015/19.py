from utils import getInput, part1, part2
from collections import defaultdict
from re import findall


def distinctAfterOneReplacement(molecule: tuple[str],
                                rules: dict[str, set[str]]) -> int:
    createdMolecules = set()
    for index, element in enumerate(molecule):
        for replacedWith in rules[element]:
            createdMolecules.add("".join(molecule[:index]
                                         + (replacedWith,)
                                         + molecule[index + 1:]))
    return len(createdMolecules)


def replacementNeededFromAnElectron(molecule: tuple[str]) -> int:
    # As you may have noticed, this solution does not even take the rules into
    # consideration. The solution builds from observations from the rules in the puzzle
    # input. The correctness of the solution is not guaranteed, however reddit threads
    # corroborate that it generally works. At most, the literals "Rn", "Ar" and "Y" may
    # need adjustment.

    # So, the solution works as follows:
    # The rules are only of these general types:
    #   ξ -> ζ θ
    #   ξ -> ζ Rn θ Ar
    #   ξ -> ζ Rn θ Y φ Ar
    #   ξ -> ζ Rn θ Y φ Y η Ar
    #   while the elements Rn, Ar and Y are terminal (do not appear on the left side of
    #   any rule).
    #
    # Thus, With each rule application, the molecule grows by:
    #   1
    #   or 1 and Rn and Ar
    #   or 1 and Rn and Ar, and 1 and Y
    #   or 1 and Rn and Ar, and 1 and Y, and 1 and Y
    #
    # This means that all derivations producing some molecule using the provided grammar
    # (set of rules) have a specific number of production rule applications.
    #
    # So, we can simply ignore (subtract) the elements Rn and Ar. Then, for each Y, we
    # find, we got a free element (so we subtract 2, one for the Y and one for the added
    # element). That leaves us with the molecule parts we need to grow by one with each
    # substitution. In the end, we want to be left with one electron, so we end with 1,
    # not 0.
    return (len(molecule)
            - molecule.count("Rn")
            - molecule.count("Ar")
            - 2 * molecule.count("Y")
            - 1)


def solveDay() -> None:
    replacementRules, medicineMolecule = getInput(19, 2015).strip().split("\n\n")
    medicineMolecule = tuple(findall(r"[A-Z][a-z]?", medicineMolecule))
    transformsInto = defaultdict(set)
    for rule in replacementRules.split('\n'):
        before, after = rule.split(" => ")
        transformsInto[before].add(after)

    part1(distinctAfterOneReplacement(medicineMolecule, transformsInto))
    part2(replacementNeededFromAnElectron(medicineMolecule))


solveDay()
