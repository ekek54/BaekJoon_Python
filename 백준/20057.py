import sys

def wind(y,di,board): #현재 좌표X에서 좌표Y로의 태풍 이동에의한 모래이동을 계산해 보드에 적용해주는 함수
    N=len(board)
    di2v = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}  # 방향 벡터
    rel_di = {'U': {'u': 'u', 'd': 'd', 'l': 'l', 'r': 'r'}, 'D': {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'},
              'L': {'u': 'l', 'd': 'r', 'l': 'd', 'r': 'u'}, 'R': {'u': 'r', 'd': 'l', 'l': 'u', 'r': 'd'}}  # 상대 방향
    out=0
    sand=board[y[0]][y[1]]
    per = [('l', 0.07), ('r', 0.07), ('ll', 0.02), ('rr', 0.02), ('ld', 0.01), ('rd', 0.01), ('ru', 0.1), ('lu', 0.07),
           ('uu', 0.05),('u',-1)]
    for i in range(len(per)):
        go,percent=per[i]
        r, c = y
        for d in go:
            conv_di=rel_di[di][d]
            r+=di2v[conv_di][0]
            c+=di2v[conv_di][1]
        if 0<=r<N and 0<=c<N:
            move = int(sand * percent) if percent != -1 else sand
            sand -= move
            board[r][c] += move
        else:
            move = int(sand * percent) if percent != -1 else sand
            sand -= move
            out += move
    return out

N=int(sys.stdin.readline())
board=[list(map(int,sys.stdin.readline().split())) for i in range(N)]
