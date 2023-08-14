import sys
from math import inf

N = int(sys.stdin.readline())

H = list(map(int, sys.stdin.readline().split()))
H.sort()
select = [False for _ in range(N)]
global answer
answer = inf

def tp(elsa_size):
    global answer
    l = 0
    r = N - 1
    while l < r:
        if select[l]: l += 1;
        elif select[r]: r -= 1;
        else:
            answer = min(answer, abs(elsa_size -  (H[l] + H[r])))
            if (H[l] + H[r]) < elsa_size: l += 1
            else: r -= 1


for i in range(N - 1):
    select[i] = True
    for j in range(i + 1, N):
        select[j] = True
        elsa_size = H[i] + H[j]
        tp(elsa_size)
        select[j] = False
    select[i] = False

print(answer)