import sys


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


calc = {"+": add, "-": substract, "*": multiply}

N = int(sys.stdin.readline())
calcFormula = sys.stdin.readline()
numbers = []
symbols = []
maxDP = [0 for i in range(N // 2 + 1)]
minDP = [0 for i in range(N // 2 + 1)]
for i in range(N):
    if i % 2 == 0:
        numbers.append(int(calcFormula[i]))
    else:
        symbols.append(calcFormula[i])
if N == 1:
    print(int(calcFormula[0]))
else:
    for i in range(N // 2 + 1):
        if i == 0:
            maxDP[i] = numbers[i]
            minDP[i] = numbers[i]
        elif i == 1:
            maxDP[i] = calc[symbols[i - 1]](numbers[i - 1], numbers[i])
            minDP[i] = calc[symbols[i - 1]](numbers[i - 1], numbers[i])
        else:
            maxDP[i] = max(calc[symbols[i - 2]](maxDP[i - 2], calc[symbols[i - 1]](numbers[i - 1], numbers[i])),
                           calc[symbols[i - 1]](maxDP[i - 1], numbers[i]),calc[symbols[i - 2]](minDP[i - 2], calc[symbols[i - 1]](numbers[i - 1], numbers[i])),
                           calc[symbols[i - 1]](minDP[i - 1], numbers[i]))

            minDP[i] = min(calc[symbols[i - 2]](minDP[i - 2], calc[symbols[i - 1]](numbers[i - 1], numbers[i])),
                           calc[symbols[i - 1]](minDP[i - 1], numbers[i]),calc[symbols[i - 2]](maxDP[i - 2], calc[symbols[i - 1]](numbers[i - 1], numbers[i])),
                           calc[symbols[i - 1]](maxDP[i - 1], numbers[i]))
    print(maxDP[-1])
