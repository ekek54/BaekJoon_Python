#벽 또는 자기자신의 몸ㅁ과 부딪히면 게임 끝
#보드의 끝은 벽이다.
#행렬 좌표 1부터 시작
#뱀은 맨위 맨좌측(0,0)에서 시작하여 오른쪽(0,1)을 향한다.
#먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
#만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
#만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다
#몇 초에 끝나는지 계산
import sys
from collections import deque
di="R"
snake=deque()
snake.append([0,0])
di_v = {"U":(-1,0),"D":(1,0), "L":(0,-1), "R":(0,1)}
di_chg = {"U":{'L':'L', 'D':'R'}, "D":{'L':'R', 'D':'L'}, "L":{'L':'D', 'D':'U'}, "R":{'L':'U', 'D':'D'}}
N = int(sys.stdin.readline())
board=[[0 for j in range(N)] for i in range(N)] #1: 사과 2: 뱀
board[0][0] = 2
time=0
K = int(sys.stdin.readline())
for _ in range(K):
    i,j = map(int,sys.stdin.readline().split())
    board[i-1][j-1]=1
L = int(sys.stdin.readline())
breaker = False
for i in range(L+1):
    if i<L:
        X, C = sys.stdin.readline().split()
        X = int(X)
    else:
        X=10001
    while X>time: #X초간 이동
        #print(time)
        #for i in range(N):
        #    print(board[i])
        #print('\n')
        time+=1
        head=snake[-1][:]
        head[0] += di_v[di][0]
        head[1] += di_v[di][1]
        if not(0 <= head[0] < N and 0 <= head[1] < N) or board[head[0]][head[1]]==2:
            print(time)
            breaker = True
            break
        else:
            if board[head[0]][head[1]]==1:
                board[head[0]][head[1]] = 2
                snake.append(head)
            else:
                tail=snake.popleft()
                board[tail[0]][tail[1]] = 0
                board[head[0]][head[1]] = 2
                snake.append(head)
    di=di_chg[di][C] #방향 전환
    if breaker:
        break