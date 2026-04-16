from utils import getInput, bothParts, RememberMax
from re import findall
import numpy as np


def parseIngredients() -> tuple[np.ndarray, np.ndarray]:
    data = np.array(list(map(int, findall(r"-?\d+", getInput(15, 2015))))).reshape(4, 5)
    return data[:, :4].T, data[:, -1]


def cookieScore(quantities: np.ndarray, properties: np.ndarray) -> int:
    return (properties @ quantities.T).clip(0).prod()


def replacesAMeal(quantities, calorieStats) -> bool:
    return (quantities * calorieStats).sum() == 500


def findBestRecipe() -> tuple[int, int]:
    properties, calorieStats = parseIngredients()
    bestScore = RememberMax()
    bestScoreMealReplacement = RememberMax()
    for frosting in range(0, 101):
        for candy in range(0, 101 - frosting):
            for butterscotch in range(0, 101 - frosting - candy):
                sugar = 100 - frosting - candy - butterscotch
                recipe = np.array((frosting, candy, butterscotch, sugar))
                score = cookieScore(recipe, properties)
                bestScore.newValueToConsider(score)
                if replacesAMeal(recipe, calorieStats):
                    bestScoreMealReplacement.newValueToConsider(score)
    return bestScore.getValue(), bestScoreMealReplacement.getValue()


def solveDay() -> None:
    bothParts(*findBestRecipe())


solveDay()
