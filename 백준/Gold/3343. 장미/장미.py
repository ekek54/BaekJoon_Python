import sys
from math import inf

N, A, B, C, D = map(int, sys.stdin.readline().split())
l = 0
r = (N - 1) // A + 1
if B * C > D * A:
    A, B, C, D = C, D, A, B
answer = inf
for i in range(A):
    tmp = D * i
    if N - i * C < 0:
        a = 0
    else:
        a = ((N - i * C) - 1) // A + 1
    tmp += a * B
    answer= min(answer, tmp)
print(answer)