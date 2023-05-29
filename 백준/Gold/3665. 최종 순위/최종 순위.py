import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    last_result = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    adj_matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            adj_matrix[last_result[i]][last_result[j]] = 1
    m = int(sys.stdin.readline())
    swaps = [tuple(map(lambda x: int(x) - 1, sys.stdin.readline().split())) for i in range(m)]
    for swap in swaps:
        a, b = swap
        adj_matrix[a][b], adj_matrix[b][a] = adj_matrix[b][a], adj_matrix[a][b]

    indegrees = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                indegrees[j] += 1
    que = deque()
    for i in range(n):
        if indegrees[i] == 0:
            que.append(i)
    answer = ''
    order = []
    while que:
        if len(que) >= 2:
            answer = '?'
            break
        cur_team = que.popleft()
        order.append(cur_team + 1)
        for i in range(n):
            if adj_matrix[cur_team][i] == 0: continue
            indegrees[i] -= 1
            if indegrees[i] == 0:
                que.append(i)
    if answer == '?':
        print(answer)
    elif len(order) == n:
        print(*order)
    else:
        print("IMPOSSIBLE")