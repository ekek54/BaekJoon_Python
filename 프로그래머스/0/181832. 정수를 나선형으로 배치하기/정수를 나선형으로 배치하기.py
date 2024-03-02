def solution(n):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    cur_r = 0
    cur_c = 0
    num = 1
    board = [[0 for j in range(n)] for i in range(n)]
    d = 0
    
    def oob(r, c):
        return not(0 <= r < n and 0 <= c < n)
    
    while num <= n ** 2:
        # print(cur_r, cur_c)
        board[cur_r][cur_c] = num
        nr = cur_r + dr[d]
        nc = cur_c + dc[d]
        if oob(nr, nc) or board[nr][nc] != 0:
            d = (d + 1) % 4
            cur_r += dr[d]
            cur_c += dc[d]
        else:
            cur_r = nr
            cur_c = nc
        num += 1
    return board