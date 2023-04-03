import sys
input=sys.stdin.readline
from collections import deque

def Find(x):

    if x!=disjoint[x]:
        disjoint[x]=Find(disjoint[x])
    return disjoint[x]

N,M,K=map(int,input().split())

edge=deque()

for i in range(M):

    u,v=map(int,input().split())

    edge.append((i+1,u,v))

for i in range(K):

    disjoint = [_ for _ in range(N + 1)] ; total=0

    for j in range(len(edge)):

        x=Find(edge[j][1])
        y=Find(edge[j][2])

        if x!=y:
            if x>y:
                disjoint[x]=y
            else:
                disjoint[y]=x
            total+=edge[j][0]

    check=set()

    for j in range(1,N+1):

        if Find(j) not in check:
            check.add(Find(j))

    if len(check)>1:
        print(0 , end=" ")
    else:
        print(total, end=" ")
    edge.popleft()