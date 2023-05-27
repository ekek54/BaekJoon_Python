import sys


def pb(board):
    for i in range(len(board)):
        print(board[i])
    print('')


n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
max_size = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            if i - 1 >= 0 and j - 1 >= 0:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
        max_size = max(board[i][j], max_size)
print(max_size ** 2)