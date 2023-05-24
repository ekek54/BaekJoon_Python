import sys


def find(parent, a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent, parent[a])
        return parent[a]


def union(parent, a, b):
    A = find(parent, a)
    B = find(parent, b)
    if A < B:
        parent[B] = A
    elif A > B:
        parent[A] = B
    return


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = [i for i in range(N)]
cityMap = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
adjList = []
for i in range(N):
    for j in range(i, N):
        if cityMap[i][j] == 1:
            adjList.append((i, j))
plan = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
for adj in adjList:
    a, b = adj
    union(parent, a, b)
tmp = find(parent, plan[0])
answer = "YES"
for city in plan:
    if find(parent, city) != tmp:
        answer = "NO"
print(answer)