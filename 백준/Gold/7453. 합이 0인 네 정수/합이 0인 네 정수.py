import sys

N = int(sys.stdin.readline())
A = []
B = []
C = []
D = []
for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = {}
for i in range(N):
    for j in range(N):
        tmp_sum = A[i] + B[j]
        if tmp_sum in AB:
            AB[tmp_sum] += 1
        else:
            AB[tmp_sum] = 1

answer = 0

for c in C:
    for d in D:
        v = -(c + d)
        if v in AB:
            answer += AB[v]
print(answer)