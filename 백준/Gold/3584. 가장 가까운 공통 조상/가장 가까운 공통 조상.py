import sys
from math import inf

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    parent_list = [[] for _ in range(N)]
    visit = [False for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        parent_list[b].append(a)
    A, B = map(int, sys.stdin.readline().split())
    A -= 1
    B -= 1
    cur_node = A
    visit[cur_node] = True
    while parent_list[cur_node]:
        cur_node = parent_list[cur_node][0]
        visit[cur_node] = True
    cur_node = B
    if visit[cur_node]:
        print(cur_node + 1)
        continue
    while parent_list[cur_node]:
        cur_node = parent_list[cur_node][0]
        if visit[cur_node]:
            print(cur_node + 1)
            break
        visit[cur_node] = True