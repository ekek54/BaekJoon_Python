import sys
from collections import deque
import copy
N,M=map(int,sys.stdin.readline().split())
map=[list(sys.stdin.readline().rstrip('\n')) for i in range(N)]
que=deque()
que.append([map,0,-100])
answer=0

def move(board,dir): #dir = 0:상 1:하 2:좌 3:우
    change=copy.deepcopy(board)
    status=1 #상태정보 1:두 공이 존재 2:빨간 공만 나감 3:파랑 공나감
    if dir==0:
        for i in range(M):
            idx = -1
            for j in range(N):
                if change[j][i]=='#':
                    idx=j+1
                elif change[j][i]=='.':
                    continue
                elif change[j][i] == 'O':
                    idx = j
                else:
                    if idx==j:
                        idx+=1
                    else:
                        if change[idx][i]=='.':
                            change[idx][i]=change[j][i]
                            change[j][i]='.'
                            idx+=1
                        elif change[idx][i]=='O':
                            if change[j][i]=='R':
                                change[j][i] = '.'
                                if status==1:
                                    status=2
                            elif change[j][i]=='B':
                                change[j][i] = '.'
                                status=3
    elif dir==1:
        for i in range(M):
            idx = N
            for j in range(N):
                #print(change[(N-1)-j][i],idx)
                if change[(N-1)-j][i]=='#':
                    idx=(N-1)-j-1
                elif change[(N-1)-j][i]=='.':
                    continue
                elif change[(N-1)-j][i] == 'O':
                    idx = (N-1)-j
                else:
                    if idx==(N-1)-j:
                        idx-=1
                    else:
                        if change[idx][i]=='.':
                            change[idx][i]=change[(N-1)-j][i]
                            change[(N-1)-j][i]='.'
                            idx-=1
                        elif change[idx][i]=='O':
                            if change[(N-1)-j][i]=='R':
                                change[(N - 1) - j][i] = '.'
                                if status == 1:
                                    status = 2
                            elif change[(N-1)-j][i]=='B':
                                change[(N - 1) - j][i] = '.'
                                status=3
    elif dir==2:
        for i in range(N):
            idx = -1
            for j in range(M):
                if change[i][j]=='#':
                    idx=j+1
                elif change[i][j]=='.':
                    continue
                elif change[i][j] == 'O':
                    idx = j
                else:
                    if idx==j:
                        idx+=1
                    else:
                        if change[i][idx]=='.':
                            change[i][idx]=change[i][j]
                            change[i][j]='.'
                            idx+=1
                        elif change[i][idx]=='O':
                            if change[i][j]=='R':
                                change[i][j] = '.'
                                if status == 1:
                                    status = 2
                            elif change[i][j]=='B':
                                change[i][j] = '.'
                                status=3
    elif dir==3:
        for i in range(N):
            idx = M
            for j in range(M):
                if change[i][(M-1)-j]=='#':
                    idx=(M-1)-j-1
                elif change[i][(M-1)-j]=='.':
                    continue
                elif change[i][(M-1)-j]=='O':
                    idx = (M-1)-j
                else:
                    if idx==(M-1)-j:
                        idx-=1
                    else:
                        if change[i][idx]=='.':
                            change[i][idx]=change[i][(M-1)-j]
                            change[i][(M-1)-j]='.'
                            idx-=1
                        elif change[i][idx]=='O':
                            if change[i][(M-1)-j]=='R':
                                change[i][(M-1)-j] = '.'
                                if status == 1:
                                    status = 2
                            elif change[i][(M-1)-j]=='B':
                                change[i][(M-1)-j] = '.'
                                status=3

    return [change,status]
def printboard(board):
    for i in range(N):
        print(board[i])
    print("\n")
while que:

    breaker=False
    cur_board,cnt,ld=que.popleft()
    #print(cnt,ld)
    #printboard(cur_board)
    if cnt==10:
        answer=-1
        break
    #print(cur_board,cnt)
    for i in range(4):
        if ld+i==1:
            continue
        if ld+i==5:
            continue
        change,status=move(cur_board,i)
        if status==1:
            que.append([change,cnt+1,i])
        elif status==2:
            breaker=True
            answer=cnt+1
            break
    if breaker:
        break

print(answer)