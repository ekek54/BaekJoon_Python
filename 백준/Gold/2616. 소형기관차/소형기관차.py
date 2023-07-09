import sys

input = sys.stdin.readline
N = int(input())
trains = list(map(int, input().split()))
K = int(input())
acc_sums = [0]
acc = 0
for i in range(N):
    acc += trains[i]
    acc_sums.append(acc)

# print(acc_sums)


def range_sum(i, j):
    if i < 0: i = 0
    return acc_sums[j] - acc_sums[i]


# print(range_sum(2, 5))

DP = [[0 for j in range(N + 1)] for i in range(4)]
for i in range(1, 4):
    for j in range(K * i, N + 1):
        DP[i][j] = max(DP[i][j - 1], DP[i - 1][j - K] + range_sum(j - K, j))
print(DP[3][N])
