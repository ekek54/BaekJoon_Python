import sys
from math import inf

T = int(sys.stdin.readline())
for t in range(T):
    k, n = map(int, sys.stdin.readline().split())
    classes = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
    A = []
    B = []
    for i in range(n):
        for j in range(n):
            A.append(classes[0][i] + classes[1][j])
            B.append(classes[2][i] + classes[3][j])
    l = 0
    r = len(B) - 1
    gap = inf
    answer = 0
    A.sort()
    B.sort()
    # print(A)
    # print(B)
    while l < len(A) and 0 <= r:
        candid = A[l] + B[r]
        # print(answer, gap)
        # print(candid)
        if gap > abs(candid - k):
            gap = abs(candid - k)
            answer = candid
        elif gap == abs(candid - k) and answer > candid:
            gap = abs(candid - k)
            answer = candid
        if candid <= k:
            l += 1
        else:
            r -= 1
    print(answer)
