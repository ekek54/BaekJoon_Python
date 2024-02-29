import sys


def pb(board):
    for i in range(len(board)):
        print(*board[i])


N, M = map(int, sys.stdin.readline().split())
H = [[0 for j in range(N + M - 1)] for i in range(N + M - 1)]
board = [list(map(lambda x: -int(x), sys.stdin.readline().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        H[M // 2 + i][M // 2 + j] = board[i][j]
answer = [[0 for j in range(N)] for i in range(N)]
acc2 = [[0 for j in range(N + M)] for i in range(N + M)]
for i in range(N - M // 2):
    for j in range(N - M // 2):
        acc2[M // 2 + i + M // 2][M // 2 + j + M // 2] = H[M // 2 + i][M // 2 + j] + acc2[M // 2 + i - M // 2 - 1][
            M // 2 + j + M // 2] + acc2[M // 2 + i + M // 2][M // 2 + j - M // 2 - 1] - acc2[M // 2 + i - M // 2 - 1][
                                                             M // 2 + j - M // 2 - 1]

for i in range(N - M // 2):
    for j in range(N - M // 2):
        answer[i][j] = acc2[i + M // 2][j + M // 2] - acc2[i + M // 2 - 1][j + M // 2] - acc2[i + M // 2][
            j + M // 2 - 1] + acc2[i + M // 2 - 1][j + M // 2 - 1]
# pb(acc2)
# print("---")
pb(answer)
