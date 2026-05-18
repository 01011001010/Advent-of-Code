from utils import getInput, part1, part2
from re import findall


# This could just as well be solved with networkx, where component count and size exist.
# In this case it wasn't a complicated algorithm, and more fun to implement by hand :)


class Village:
    class Programme:
        def __init__(self, ID: str) -> None:
            self.ID = ID
            self.communicatesWith = set()

        def __hash__(self) -> int:
            return self.ID.__hash__()

        def addConnections(self, programmes: dict, IDs: list[str]) -> None:
            for connection in IDs:
                if connection not in programmes:
                    programmes[connection] = Village.Programme(connection)
                self.communicatesWith.add(programmes[connection])

        def listGroup(self) -> set["Village.Programme"]:
            reached: set["Village.Programme"] = {self}
            reachNext = self.communicatesWith.copy()
            while reachNext:
                reaching = reachNext.pop()
                reached.add(reaching)
                reachNext.update(reaching.communicatesWith - reached)
            return reached

        def groupSize(self) -> int:
            return len(self.listGroup())

    def __init__(self) -> None:
        self.programmes = {}
        for ID, *communicatesWith in map(lambda info: findall(r"\d+", info),
                                         getInput(12, 2017).strip().splitlines()):
            if ID not in self.programmes:
                self.programmes[ID] = self.Programme(ID)
            self.programmes[ID].addConnections(self.programmes, communicatesWith)

    def groupSize(self, ID: str) -> int:
        return self.programmes[ID].groupSize()

    def groupCount(self) -> int:
        notCounted = set(self.programmes.values())
        groupCount = 0
        while notCounted:
            programme = notCounted.pop()
            groupCount += 1
            notCounted.difference_update(programme.listGroup())
        return groupCount


def solveDay() -> None:
    village = Village()

    part1(village.groupSize('0'))
    part2(village.groupCount())


solveDay()
