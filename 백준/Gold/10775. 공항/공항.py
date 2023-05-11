import sys
from collections import deque
sys.setrecursionlimit(100000)
G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
g = [int(sys.stdin.readline()) - 1 for _ in range(P)]
nxt = [i for i in range(G)]

def find(a):
    if a == nxt[a]:
        return a
    if nxt[a] == -1: return -1
    nxt[a] = find(nxt[a])
    return nxt[a]
answer = 0

for i in range(P):
    #print(nxt)
    #print(find(g[i]))
    if find(g[i]) == -1:
        break
    else:
        nxt[find(g[i])] = find(g[i]) - 1
        answer += 1
    #print(answer)

print(answer)