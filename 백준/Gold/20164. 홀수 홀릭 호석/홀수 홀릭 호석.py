import sys
from math import inf

N = sys.stdin.readline().rstrip()


def max_solution(N):
    odd_cnt = 0
    for i in range(len(N)):
        if int(N[i]) % 2 == 1:
            odd_cnt += 1
    if len(N) == 1:
        return odd_cnt

    ret = 0

    if len(N) == 2:
        return odd_cnt + max_solution(str(int(N[:1]) + int(N[1:])))

    if len(N) >= 3:
        for i in range(1, len(N) - 1):
            for j in range(i + 1, len(N)):
                a = N[: i]
                b = N[i: j]
                c = N[j: len(N)]
                ret = max(ret, max_solution(str(int(a) + int(b) + int(c))))
        return ret + odd_cnt


def min_solution(N):
    odd_cnt = 0
    for i in range(len(N)):
        if int(N[i]) % 2 == 1:
            odd_cnt += 1
    if len(N) == 1:
        return odd_cnt

    ret = inf

    if len(N) == 2:
        return odd_cnt + min_solution(str(int(N[:1]) + int(N[1:])))

    if len(N) >= 3:
        for i in range(1, len(N) - 1):
            for j in range(i + 1, len(N)):
                a = N[: i]
                b = N[i: j]
                c = N[j: len(N)]
                ret = min(ret, min_solution(str(int(a) + int(b) + int(c))))
        return ret + odd_cnt


print(min_solution(N), max_solution(N))
