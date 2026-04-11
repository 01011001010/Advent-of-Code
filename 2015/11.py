from utils import getInput, part1, part2
from string import ascii_lowercase
from re import findall, search


class Password:
    def __init__(self, oldPassword) -> None:
        self.nextLetter = {original: new
                           for original, new
                           in zip(ascii_lowercase,
                                  ascii_lowercase[1:] + ascii_lowercase)}

        self._password = list(oldPassword)
        self.consecutivePattern = "(?:" + "|".join(map(lambda t: "".join(t),
                                                       zip(ascii_lowercase,
                                                           ascii_lowercase[1:],
                                                           ascii_lowercase[2:]))) + ")"

    def password(self) -> str:
        return "".join(self._password)

    def findNextPassword(self) -> str:
        # increment until approved by the Security-Elf
        self.increaseLetter(len(self._password) - 1)
        while not self.securityElfApproved():
            self.increaseLetter(len(self._password) - 1)
        return self.password()

    def increaseLetter(self, position: int) -> None:
        if position < 0:
            raise NotImplementedError("Next password will increase in length. "
                                      "This was not expected.")
        self._password[position] = self.nextLetter[self._password[position]]
        if self._password[position] == 'a':
            self.increaseLetter(position - 1)

    def securityElfApproved(self) -> bool:
        # passwords must include one increasing straight of at least three letters
        if not search(self.consecutivePattern, self.password()):
            return False

        # passwords may not contain the letters i, o, or l
        if search(r"iol", self.password()):
            return False

        # passwords must contain at least two different non-overlapping pairs of letters
        if len(set(findall(r"(.)\1", self.password()))) < 2:
            return False

        return True


def solveDay() -> None:
    password = Password(getInput(11, 2015).strip())
    part1(password.findNextPassword())
    part2(password.findNextPassword())


solveDay()
