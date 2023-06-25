import sys
import heapq
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ground = [[5 for j in range(N)] for i in range(N)]
trees = [[deque() for j in range(N)] for i in range(N)]
dead_trees = [[[] for j in range(N)] for i in range(N)]
input_tree = []
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    input_tree.append((x, y, z))
input_tree.sort(key=lambda x: x[2])
for tree in input_tree:
    r, c, z = tree
    trees[r][c].append(z)


def winter():
    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]


def spring():
    tmp = deque()
    for i in range(N):
        for j in range(N):
            while trees[i][j]:
                cur_tree = trees[i][j].popleft()
                if ground[i][j] >= cur_tree:
                    ground[i][j] -= cur_tree
                    tmp.append(cur_tree + 1)
                else:
                    dead_trees[i][j].append(cur_tree)
            tmp, trees[i][j] = trees[i][j], tmp


def summer():
    for i in range(N):
        for j in range(N):
            while dead_trees[i][j]:
                ground[i][j] += dead_trees[i][j].pop() // 2


def fall():
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(N):
        for j in range(N):
            for tree in trees[i][j]:
                if tree % 5 == 0:
                    for k in range(8):
                        nr = i + dr[k]
                        nc = j + dc[k]
                        if 0 <= nr < N and 0 <= nc < N:
                            trees[nr][nc].appendleft(1)
# winter()
def pb(board):
    for i in range(len(board)):
        print(board[i])
    print()
for _ in range(K):
    # pb(ground)
    # pb(trees)
    spring()
    # pb(ground)
    # pb(trees)
    summer()
    # pb(ground)
    # pb(trees)
    fall()
    # pb(ground)
    # pb(trees)
    winter()
    # pb(ground)
    # pb(trees)
# pb(trees)
answer = 0

for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])
print(answer)