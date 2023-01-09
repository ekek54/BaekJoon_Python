from sys import stdin
N,M=map(int,stdin.readline().split())
board=[list(map(int,stdin.readline().split())) for i in range(N)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
chk=[[False for j in range(M)] for i in range(N)]
res=[]

global ans
ans=0

def dfs(x,y,cnt,square):
    global ans

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if chk[nx][ny]:
                continue
            else:
                if cnt == 2:
                    ans = max(ans, square+board[nx][ny])
                    continue
                chk[nx][ny] = True
                dfs(nx,ny,cnt+1,square+board[nx][ny])
                chk[nx][ny] = False

for i in range(N):
    for j in range(M):
        chk[i][j] = True
        dfs(i,j,0,board[i][j])
        chk[i][j] = False
        s=0
        tmp=0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                s+=1
                tmp+=(board[nx][ny])
        if s==3:
            ans=max(ans,tmp+board[i][j])
        elif s==4:
            for k in range(4):
                ans = max(ans,tmp + board[i][j]-board[i+dx[k]][j+dy[k]])
        res=[]
print(ans)