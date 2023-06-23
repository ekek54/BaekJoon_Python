import sys

results = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
for i in range(4):
    results[i] = [[results[i][j * 3], results[i][j * 3 + 1], results[i][j * 3 + 2]] for j in range(6)]
# print(results)
matchup = []
for i in range(6):
    for j in range(i + 1, 6):
        matchup.append((i, j))
# print(matchup)
result = [[0, 0, 0] for _ in range(6)]


# def same(a, b):
#     for i in range(6):
#         for j in range(3):
#             if a[i][j] != b[i][j]:
#                 return False
#     return

def dfs(cnt, target):
    if cnt == 15:
        return True
    a, b = matchup[cnt]
    for i in range(3):
        result[a][i] += 1
        result[b][2 - i] += 1
        if result[a][i] <= target[a][i] and result[b][2 - i] <= target[b][2 - i]:
            if dfs(cnt + 1, target): return True
        result[a][i] -= 1
        result[b][2 - i] -= 1
    return False

def valid(a):
    for i in range(6):
        if sum(a[i]) != 5:
            return False
    return True

answer = []

for i in range(4):
    result = [[0, 0, 0] for _ in range(6)]
    answer.append(0 if not valid(results[i]) else 1 if dfs(0, results[i]) else 0)
print(*answer)