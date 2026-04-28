from utils import getInput, part1, part2


def solveCaptcha(captcha: list[int], shiftByOne: bool) -> int:
    shift = 1 if shiftByOne else len(captcha) // 2
    return sum(map(lambda pair: pair[0],
                   filter(lambda pair: pair[0] == pair[1],
                          zip(captcha, captcha[shift:] + captcha[:shift]))))


def solveDay() -> None:
    captcha = list(map(int, list(getInput(1, 2017).strip())))
    part1(solveCaptcha(captcha, True))
    part2(solveCaptcha(captcha, False))


solveDay()
