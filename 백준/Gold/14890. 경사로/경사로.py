<<<<<<< Updated upstream
import sys

N, L = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for i in range(N)]


def isPossibleToCross(road, L):
    roadLength = len(road)
    isSet = [False for _ in range(roadLength)]
    for idx in range(roadLength - 1):
        if road[idx] + 1 == road[idx + 1]:
            if not setUpStair(road, isSet, idx, L):
                return False
        elif road[idx] - 1 == road[idx + 1]:
            if not setDownStair(road, isSet, idx, L):
                return False
        elif road[idx] == road[idx + 1]:
            continue
        else:
            return False
    return True


def setUpStair(road, isSet, idx, L):
    curFloor = road[idx]
    for i in range(L):
        if idx - i < 0 or road[idx - i] != curFloor or isSet[idx - i]:
            return False
    for i in range(L):
        isSet[idx - i] = True
    return True


def setDownStair(road, isSet, idx, L):
    curFloor = road[idx + 1]
    for i in range(L):
        if idx + i + 1 >= len(road) or road[idx + i + 1] != curFloor or isSet[idx + i + 1]:
            return False
    for i in range(L):
        isSet[idx + i + 1] = True
    return True


cnt = 0
for i in range(N):
    row = [board[i][j] for j in range(N)]
    col = [board[j][i] for j in range(N)]
    if isPossibleToCross(row, L):
        #print(row)
        cnt += 1
    if isPossibleToCross(col, L):
        #print(col)
        cnt += 1
print(cnt)
=======
import sys

def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

calc = {"+":add, "-":substract, "*":multiply}


N = int(sys.stdin.readline())
calcFormula = sys.stdin.readline()
numbers = []
symbols = []
DP=[0 for i in range(N//2+1)]
for i in range(N):
    if i%2 == 0:
        numbers.append(calcFormula[i])
    else:
        symbols.append(calcFormula[i])
if N == 1:
    print(int(calcFormula[0]))
else:
    for i in range(N//2+1):
        if i == 0:
            DP[i] = numbers[i]
        elif i == 1:
            DP[i] = calc[symbols[i]](numbers[i-1],numbers[i])
        else:
            DP[i] = max(calc[symbols[i-1]](DP[i-2],calc[symbols[i]](numbers[i-1],numbers[i])),calc[symbols[i]](DP[i-1],numbers[i]))
print(DP)
>>>>>>> Stashed changes
