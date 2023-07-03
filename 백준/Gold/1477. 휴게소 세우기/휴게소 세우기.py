import sys
import heapq

N, M, L = map(int, sys.stdin.readline().split())
spots = list(map(int, sys.stdin.readline().split()))
spots.append(0)
spots.append(L)
spots.sort()
dists = []
for i in range(N + 1):
    dists.append(spots[i + 1] - spots[i])
# print(dists)

def calc(m):
    result = 0
    for i in range(len(dists)):
        result += dists[i] // m
        if dists[i] % m == 0:
            result -= 1
    # print(m, result)
    return result

l = 1
r = L
while l <= r:
    # print(l, r)
    mid = (l + r) // 2
    if calc(mid) <= M:
        r = mid - 1
    else:
        l = mid + 1
print(l)