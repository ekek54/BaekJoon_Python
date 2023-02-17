import sys
di2v = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}  # 방향 벡터
def wind(y,di,board): #현재 좌표X에서 좌표Y로의 태풍 이동에의한 모래이동을 계산해 보드에 적용해주는 함수
    N=len(board)
    rel_di = {'U': {'u': 'U', 'd': 'D', 'l': 'L', 'r': 'R'}, 'D': {'u': 'D', 'd': 'U', 'l': 'R', 'r': 'L'},
              'L': {'u': 'L', 'd': 'R', 'l': 'D', 'r': 'U'}, 'R': {'u': 'R', 'd': 'L', 'l': 'U', 'r': 'D'}}  # 상대 방향
    out=0
    sand=board[y[0]][y[1]]
    per = [('l', 0.07), ('r', 0.07), ('ll', 0.02), ('rr', 0.02), ('ld', 0.01), ('rd', 0.01), ('ru', 0.1), ('lu', 0.1),
           ('uu', 0.05),('u',-1)]
    for i in range(len(per)):
        go,percent=per[i]
        r, c = y
        for d in go:
            conv_di=rel_di[di][d]
            r+=di2v[conv_di][0]
            c+=di2v[conv_di][1]
        if 0<=r<N and 0<=c<N:
            move = int(board[y[0]][y[1]] * percent) if percent != -1 else sand
            sand -= move
            board[r][c] += move
        else:
            move = int(board[y[0]][y[1]] * percent) if percent != -1 else sand
            sand -= move
            out += move
    board[y[0]][y[1]]=0
    return out

N=int(sys.stdin.readline())
board=[list(map(int,sys.stdin.readline().split())) for i in range(N)]
x = (N//2, N//2)
spin = ('L', 'D', 'R', 'U')
out = 0
idx=0
cnt=1
switch=0
while x != (0,0):
    di=spin[idx]
    for _ in range(cnt):
        y=(x[0]+di2v[di][0],x[1]+di2v[di][1])
        out+=wind(y,di,board)
        x=y[:]
        if x == (0,0):
            break
    switch+=1
    if switch%2==0:
        cnt+=1
    idx=(idx+1)%4
print(out)