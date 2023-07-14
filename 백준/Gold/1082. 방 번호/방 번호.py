from sys import stdin
from collections import deque

N = int(stdin.readline())
P = list(map(int, stdin.readline().split()))
M = int(stdin.readline())

dp = [["" for j in range(M + 1)] for i in range(N + 1)]


def upgrade(num_str, insert_num, insert_cnt):
    if insert_cnt == 0: return num_str
    # print(num_str, insert_num, insert_cnt)
    insert_idx = 0
    for i in range(len(num_str)):
        if int(num_str[i]) > insert_num:
            insert_idx = i
    result = num_str[:insert_idx] + (str(insert_num) * insert_cnt) + num_str[insert_idx:]
    # print(result)
    # if result[0] == "0":
    #     return "0"
    return result


def my_max(a, b):
    if len(a) > len(b):
        return a
    elif len(a) < len(b):
        return b
    else:
        for i in range(len(a)):
            if a[i] == b[i] : continue
            elif a[i] > b[i]: return a
            else: return b
    return a

for i in range(1, N + 1):
    for j in range(1, M + 1):
        for k in range(j // P[i - 1] + 1):
            dp[i][j] = my_max(dp[i][j], upgrade(dp[i - 1][j - P[i - 1] * k], i - 1, k))
# print(dp)
answer = ""
for i in range(1, N):
    if M - P[i] < 0:
        continue
    answer = my_max(answer, upgrade(dp[N][M - P[i]], i, 1))
# print(answer)
print(0 if len(answer) == 0 else answer)
