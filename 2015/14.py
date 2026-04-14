from utils import getInput, part1, part2
from re import findall
import numpy as np


def distanceTravelled(seconds: int, speed: int, moveTime: int, restTime: int) -> int:
    return (speed * ((seconds//(moveTime+restTime)) * moveTime +
                     min((seconds % (moveTime+restTime)), moveTime)))


def reindeerDistances(seconds: int, reindeer: list[tuple[int, ...]]) -> np.ndarray:
    # Creates a 'seconds x n-reindeer' matrix, where each row represents a reindeer and
    # each column i, the distance that reindeer travelled by a given reindeer in i
    # seconds
    # The matrix is created as follows:
    # - for each reindeer, create a sequence of distance covered in each second for the
    #   given duration
    # - compute cumulative sums for each reindeer
    return np.cumsum([np.tile(np.concatenate((np.repeat(speed, moveTime),
                                              np.repeat(0, restTime))),
                              (seconds // (moveTime + restTime)) + 1)[:seconds]
                      for speed, moveTime, restTime in reindeer], axis=1)


def scoreOfWinner(distancesInTime: np.ndarray) -> int:
    # Find the winning score:
    # - find lead distance for each time increment
    # - for each reindeer, find time increments when in lead and award individual points
    # - sum up points per reindeer
    # - find the winner
    return np.sum(distancesInTime == distancesInTime.max(axis=0), axis=1).max()


def solveDay() -> None:
    seconds = 2503
    reindeer = list(map(lambda stats: tuple(map(int, findall(r"\d+", stats))),
                        getInput(14, 2015).strip().splitlines()))

    part1(max(map(lambda reindeer: distanceTravelled(seconds, *reindeer), reindeer)))
    part2(scoreOfWinner(reindeerDistances(seconds, reindeer)))


solveDay()
