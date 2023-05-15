import sys
from collections import deque

# 홀수 개수가 K 이하인 연속 부분 수열 짝수의 개수 max
# 투포인터 l: 연속부분 수열 시작점, r: 끝점
# case1 현재 홀수의 개수가 K 미만이면, r++
# case2 현재 홀수의 개수가 K 이면, l++
N, K = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))
l = 0
r = 0
odd_cnt = 0 if S[0] % 2 == 0 else 1
even_cnt = 1 if S[0] % 2 == 0 else 0
answer = even_cnt
while l <= r < N - 1:
    #print(even_cnt, odd_cnt)
    if odd_cnt <= K:
        r += 1
        if S[r] % 2 == 0:
            even_cnt += 1
            answer = max(answer, even_cnt)
        else:
            odd_cnt += 1
    else:
        l += 1
        if S[l - 1] % 2 == 0:
            even_cnt -= 1
        else:
            odd_cnt -= 1
print(answer)