from sys import stdin
from collections import deque

S = stdin.readline().rstrip();
T = stdin.readline().rstrip();


def solution(S: str, T: str):
    B_gap = T.count('B') - S.count('B')
    # print(B_gap)
    if B_gap % 2 == 0:
        T = deque(T)
        left_B_cnt = B_gap // 2
        right_B_cnt = B_gap // 2
        if B_gap > 0 and T[0] == "A": return False
    else:
        T = deque(reversed(T))
        left_B_cnt = B_gap // 2
        right_B_cnt = B_gap // 2 + 1
        if T[-1] == "A": return False


    r_cnt = 0
    while r_cnt < right_B_cnt:
        if T.pop() == 'B': r_cnt += 1

    l_cnt = 0
    while l_cnt < left_B_cnt:
        if T.popleft() == 'B': l_cnt += 1

    T = "".join(T)
    if S not in T:
        return False
    if B_gap == 0:
        return T.index(S) == 0

    return not ('B' in T.replace(S, ""))
    # print(T)


print(1 if solution(S, T) else 0)