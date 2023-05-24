import sys

N, M = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)]
A.sort()
l = 0
r = 1
answer = 2000000000
while l < r < N:
    if A[r] - A[l] < M:
        r += 1
    elif A[r] - A[l] > M:
        answer = min(answer, A[r] - A[l])
        l += 1
        if l == r:
            r += 1
    else:
        answer = M
        break
print(answer)