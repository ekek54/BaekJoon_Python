from collections import deque


def get_pattern(table):
    N = len(table)
    table_org = [[table[i][j] for j in range(N)] for i in range(N)]
    patterns = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(N):
        for j in range(N):
            if table[i][j] == 0:
                continue
            else:
                que = deque()
                que.append([j, i])
                L, T, R, B = 51, 51, 0, 0

                while que:
                    cur = que.popleft()
                    x = cur[0]
                    L = min(L, x)
                    R = max(R, x)
                    y = cur[1]
                    T = min(T, y)
                    B = max(B, y)
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if ny < 0 or N <= ny or nx < 0 or N <= nx:
                            continue
                        if table[ny][nx] == 0:
                            continue
                        table[ny][nx] = 0
                        que.append([nx, ny])
                pattern = [[table_org[j][i] for i in range(L, R + 1)] for j in range(T, B + 1)]
                patterns.append(pattern)
    return patterns


def rotate(degree, board):
    N = len(board)
    M = len(board[0])
    if degree == 0:
        return board
    elif degree == 90:
        return [[board[j][i] for j in range(N-1, -1, -1)] for i in range(M)]
    elif degree == 180:
        return [[board[i][j] for j in range(M-1, -1, -1)] for i in range(N-1, -1, -1)]
    else:
        return [[board[j][i] for j in range(N)] for i in range(M-1, -1, -1)]


def solution(game_board, table):
    table_pattern = get_pattern(table)
    game_board = [[0 if game_board[i][j] else 1 for j in range(len(game_board))] for i in range(len(game_board))]
    board_pattern = get_pattern(game_board)
    blank = 0
    print(table_pattern)
    print(board_pattern)
    for i in table_pattern:
        for idx, j in enumerate(board_pattern):
            if len(i) == len(j) and len(i[0]) == len(j[0]):
                if i == j or rotate(180, i) == j:
                    blank += sum([k.count(1) for k in j])
                    board_pattern.pop(idx)
                    break
            if len(i) == len(j[0]) and len(i[0]) == len(j):
                if rotate(90, i) == j or rotate(270, i) == j:
                    blank += sum([k.count(1) for k in j])
                    board_pattern.pop(idx)
                    break
    return blank