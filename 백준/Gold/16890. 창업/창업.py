import sys
from collections import deque

A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip())
N = len(A)
A.sort()
B.sort(reverse=True)
A = A[: N // 2 + 1 if N % 2 == 1 else N // 2]
B = B[: N // 2]
A = deque(A)
B = deque(B)
answer = ["" for _ in range(N)]
l = 0
r = N - 1
for i in range(N):
    if i % 2 == 0:
        if not B or A[0] < B[0]:
            answer[l] = A.popleft()
            l += 1
        else:
            answer[r] = A.pop()
            r -= 1
    else:
        if not A or A[0] < B[0]:
            answer[l] = B.popleft()
            l += 1
        else:
            answer[r] = B.pop()
            r -= 1

print("".join(answer))