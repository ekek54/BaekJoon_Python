import sys
from collections import deque
from math import inf


def nCr(n, r):
    r = min(r, n - r)
    if r == 0: return 1
    ret = 1
    for i in range(r):
        ret *= n - i
        ret /= i + 1
    return int(ret)


N, M ,K = map(int, sys.stdin.readline().split())
a_count = N
z_count = M
answer = ""
for i in range(N + M):
    #print(nCr(a_count - 1 + z_count, z_count), K)
    if a_count == 0:
        answer += 'z'
        z_count -= 1
    elif z_count == 0:
        answer += 'a'
        a_count -= 1
    elif nCr(a_count - 1 + z_count, z_count) >= K:
        answer += 'a'
        a_count -= 1
    else:
        answer += 'z'
        K -= nCr(a_count - 1 + z_count, z_count)
        z_count -= 1

print(answer if K == 1 else -1)