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