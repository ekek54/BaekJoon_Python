import sys
from collections import deque

board = [list(sys.stdin.readline()) for i in range(12)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
combo=0
while 1:
    boom=False
    visit = [[False for j in range(6)] for i in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] == '.':
                visit[i][j] = True
                continue
            elif visit[i][j] == True:
                continue
            else:
                #print(i,j)
                que=deque()
                visit[i][j] = True
                que.append([i,j])
                stack=[]
                while que:
                    cur = que.popleft()
                    stack.append(cur)
                    for k in range(4):
                        nx = cur[0] + dx[k]
                        ny = cur[1] + dy[k]
                        if 0 <= nx < 12 and 0 <= ny < 6:
                            if visit[nx][ny] == False and board[nx][ny]==board[cur[0]][cur[1]]:
                                visit[nx][ny]=True
                                que.append([nx,ny])
                if len(stack)>=4:
                    boom=True
                    for s in stack:
                        board[s[0]][s[1]]="."

                    for k in range(6):
                        tmp = []
                        for l in range(12):
                            if board[l][k]!='.':
                                tmp.append(board[l][k])
                                board[l][k]='.'
                        idx=-1
                        while tmp:
                            board[idx][k]=tmp.pop()
                            idx-=1


    if boom:
        combo+=1
    else: break
print(combo)