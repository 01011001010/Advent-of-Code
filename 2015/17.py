from utils import getInput, part1, part2, RememberExtreme


class MinimumCounter(RememberExtreme):
    def __init__(self) -> None:
        self.value = None
        self.count = 0

    def __str__(self) -> str:
        return str(self.count)

    def getCount(self) -> int:
        return self.count

    def newValueToConsider(self, value: int) -> None:
        if self.value is None or self.value > value:
            self.value = value
            self.count = 1
        elif self.value == value:
            self.count += 1


def countCombinations(volumeLeft: int,
                      containerSizes: list[int],
                      indexOfLargestAllowedContainer: int,
                      minimumContainerCombinationsCount: MinimumCounter,
                      usedContainerCount: int) -> int:

    # Volume perfectly matched
    if volumeLeft == 0:
        minimumContainerCombinationsCount.newValueToConsider(usedContainerCount)
        return 1

    # Remove containers larger than remaining volume from consideration
    while (indexOfLargestAllowedContainer >= 0
           and containerSizes[indexOfLargestAllowedContainer] > volumeLeft):
        indexOfLargestAllowedContainer -= 1

    # Volume left to cover negative or smaller than the smallest available container
    if indexOfLargestAllowedContainer < 0:
        return 0

    return (countCombinations((volumeLeft
                               - containerSizes[indexOfLargestAllowedContainer]),
                              containerSizes,
                              indexOfLargestAllowedContainer-1,
                              minimumContainerCombinationsCount,
                              usedContainerCount + 1)
            # ↑ Count of combinations that include the
            #   `indexOfLargestAllowedContainer`th container
            # ↓ Count of combinations that do *not* include the
            #   `indexOfLargestAllowedContainer`th container
            + countCombinations(volumeLeft,
                                containerSizes,
                                indexOfLargestAllowedContainer-1,
                                minimumContainerCombinationsCount,
                                usedContainerCount))


def solveDay() -> None:
    containerSizes = sorted(map(int, getInput(17, 2015).strip().splitlines()))
    combinationsUsingLeastContainers = MinimumCounter()
    part1(countCombinations(150,  # 150 litres of eggnog
                            containerSizes,  # using provided containers
                            len(containerSizes)-1,  # allowing all containers
                            combinationsUsingLeastContainers,  # global counter object
                            0))  # no containers used apriori
    part2(str(combinationsUsingLeastContainers))


solveDay()
