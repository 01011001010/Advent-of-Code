from utils import getInput, part1, part2
import numpy as np


class Processor:
    def __init__(self) -> None:
        self.skipSize = 0
        self.currentPosition = 0
        self.ringSize = 256
        self.state = np.arange(self.ringSize)
        data = getInput(10, 2017).strip()
        self.lengths = list(map(int, data.split(',')))
        self.lengthsByte = list(map(ord, data)) + [17, 31, 73, 47, 23]

    def reset(self) -> None:
        self.skipSize = 0
        self.currentPosition = 0
        self.ringSize = 256
        self.state = np.arange(self.ringSize)

    def processOneLength(self, length) -> None:
        # arr[mask] = arr[mask][::-1] does not preserve the order at the edge, so:
        # The circularity is simulated with double array length
        # Explanation with example:
        # reversing [] in (): (1 2 3] 4 5 6 7 [8 9) ⁽¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹⁾
        # mask:               (✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✓ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗)
        # temp:               (0 0 0 0 0 0 0 3 2 1 9 8 0 0 0 0 0 0)
        # reshaped mask:      (✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✓
        #                   +  ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗)
        #                   -------------------------
        #                     (✓ ✓ ✓ ✗ ✗ ✗ ✗ ✓ ✓)
        # reshaped temp:      (0 0 0 0 0 0 0 3 2
        #                   +  1 9 8 0 0 0 0 0 0)
        #                   -------------------------
        #                     (1 9 8 0 0 0 0 3 2)

        # Create mask specifying the position of the reverser section
        mask = np.full(self.ringSize * 2, False)
        mask[self.currentPosition: self.currentPosition + length] = True

        # Create a temporary array with the reversed section (0 elsewhere)
        temp = np.full(2 * self.ringSize, 0)
        temp[mask] = np.tile(self.state, 2)[mask][::-1]

        # Split the mask and temporary arrays and stack to return to the original size
        temp = temp.reshape((2, -1)).sum(axis=0)
        mask = mask.reshape((2, -1)).sum(axis=0, dtype=bool)

        # Migrate change to the real array state
        self.state[mask] = temp[mask]

        # Adjust pointer and skip size
        self.currentPosition += length + self.skipSize
        self.currentPosition %= self.ringSize
        self.skipSize += 1
        self.skipSize %= self.ringSize

    def process(self) -> int:
        for length in self.lengths:
            self.processOneLength(length)
        return self.state[0] * self.state[1]

    def giveHash(self) -> str:
        self.reset()
        for _ in range(64):
            for length in self.lengthsByte:
                self.processOneLength(length)
        return ''.join(f'{number:02x}'
                       for number
                       in (np.bitwise_xor.reduce(self.state[block * 16:
                                                            (block + 1) * 16])
                           for block
                           in range(16)))


def solveDay() -> None:
    processor = Processor()
    part1(processor.process())
    part2(processor.giveHash())


solveDay()
