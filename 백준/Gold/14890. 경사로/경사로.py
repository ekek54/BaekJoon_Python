import sys

N, L = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

# 1차원 배열 경로와 경사로 크기 L을 입력받아
# 건널 수 있는 경로인지 판단하는 함수
def isPossibleToCross(road, L):
    roadLength = len(road)
    isSet = [False for _ in range(roadLength)] # 경사로가 설치된 곳인지 기록하는 배열
    for idx in range(roadLength - 1):
        if road[idx] + 1 == road[idx + 1]: # 다음 칸이 1층 높으면
            if not setUpStair(road, isSet, idx, L): # 올라가는 경사로 설치 - 경사로 설치 불가면 False 반환
                return False
        elif road[idx] - 1 == road[idx + 1]: # 다음 칸이 1층 낮으면
            if not setDownStair(road, isSet, idx, L): # 내려가는 경사로 설치 - 경사로 설치 불가면 False 반환
                return False
        elif road[idx] == road[idx + 1]: # 다음 칸이 현재 층과 같으면
            continue
        else:
            return False
    return True

# 올라가는 경사로 설치하는 함수
# 다음 칸이 현재칸보다 1층 크다면 호출
# 경사로가 설치 가능하면 isSet 배열에 설치된 칸 마킹
# 설치 불가면 False 반환
def setUpStair(road, isSet, idx, L):
    curFloor = road[idx]
    for i in range(L):
        # 경사로 설치 칸이 경로를 벗어나거나, 평평하지 않거나(같은 층이 아님), 경사로가 이미 설치된 곳이라면 설치 불가
        if idx - i < 0 or road[idx - i] != curFloor or isSet[idx - i]:
            return False
    # 설치 가능하면 isSet에 마킹 후 True 반환
    for i in range(L):
        isSet[idx - i] = True
    return True


# 내려가는 경사로 설치하는 함수
# 다음 칸이 현재칸과 1층 작다면 호출
# 경사로가 설치 가능하면 isSet 배열에 설치된 칸 마킹
# 설치 불가면 False 반환
def setDownStair(road, isSet, idx, L):
    curFloor = road[idx + 1]
    for i in range(L):
        if idx + i + 1 >= len(road) or road[idx + i + 1] != curFloor or isSet[idx + i + 1]:
            return False
    for i in range(L):
        isSet[idx + i + 1] = True
    return True


cnt = 0
# 모든 행과 열에 대해 확인
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