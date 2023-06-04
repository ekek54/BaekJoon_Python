import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visit = [[False for j in range(M)] for i in range(N)]
is_r_board = [[0 for j in range(M)] for i in range(N)]
case_cnt = 0

def calc():
    result = 0
    for i in range(N):
        num_str = "0"
        for j in range(M):
            if is_r_board[i][j]:
                num_str += board[i][j]
            else:
                result += int(num_str)
                num_str = "0"
        result += int(num_str)

    for i in range(M):
        num_str = "0"
        for j in range(N):
            if not is_r_board[j][i]:
                num_str += board[j][i]
            else:
                result += int(num_str)
                num_str = "0"
        result += int(num_str)
    return result

answer = 0

def dfs(cnt: int):
    global answer
    if cnt == N * M:
        answer = max(answer, calc())
        return

    cur_r = cnt // M
    cur_c = cnt % M
    for i in range(2):
        is_r_board[cur_r][cur_c] = i
        dfs(cnt + 1)


dfs(0)
print(answer)
