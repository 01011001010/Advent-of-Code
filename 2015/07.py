from utils import getInput, part1, part2


def initialiseSignals(bOverride: int | str | None = None) -> dict[str, str | int]:
    signals = {}
    for instruction in getInput(7, 2015).strip().splitlines():  # getInput is memoised
        connection, output = instruction.strip().split(' -> ')
        signals[output] = connection
    signals['b'] = bOverride  # part 2
    return signals


def readSignal(signals: dict, wire: str) -> int:  # modifies signals dict in-place
    # reading a resolved signal
    if wire.isnumeric():
        return int(wire)

    if isinstance(signals[wire], int):
        pass  # if this were removed, we would unnecessarily evaluate all the conditions

    # resolving a complex signal, any unknown wires are resolved with recursion
    elif signals[wire].isnumeric():
        signals[wire] = int(signals[wire])
    elif ' ' not in signals[wire]:
        signals[wire] = readSignal(signals, signals[wire])
    elif 'NOT' in signals[wire]:
        signals[wire] = ~ readSignal(signals, signals[wire][len("NOT "):])
    elif 'AND' in signals[wire]:
        left, right = signals[wire].split(' AND ')
        signals[wire] = readSignal(signals, left) & readSignal(signals, right)
    elif 'OR' in signals[wire]:
        left, right = signals[wire].split(' OR ')
        signals[wire] = readSignal(signals, left) | readSignal(signals, right)
    elif 'RSHIFT' in signals[wire]:
        left, right = signals[wire].split(' RSHIFT ')
        signals[wire] = readSignal(signals, left) >> int(right)
    elif 'LSHIFT' in signals[wire]:
        left, right = signals[wire].split(' LSHIFT ')
        signals[wire] = (readSignal(signals, left) << int(right))

    return signals[wire]


def solveDay() -> None:
    signals = initialiseSignals()
    part1(readSignal(signals, 'a'))
    part2(readSignal(initialiseSignals(signals['a']), 'a'))


solveDay()
