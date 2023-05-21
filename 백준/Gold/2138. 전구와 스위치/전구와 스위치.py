import sys
from collections import deque

def turn_on(arr, i):
    arr[i - 1] = (arr[i - 1] + 1) % 2
    arr[i] = (arr[i] + 1) % 2
    if i + 1 < len(arr):
        arr[i + 1] = (arr[i + 1] + 1) % 2

N = int(sys.stdin.readline())
des = int(sys.stdin.readline().rstrip(), 2) ^ int(sys.stdin.readline().rstrip(), 2)
target = list(map(int, list(bin(des).lstrip('0b').zfill(N))))
case1 = [0 for _ in range(N)]
cnt1 = 0
case2 = [0 for _ in range(N)]
cnt2 = 1
case2[0], case2[1] = 1, 1
for i in range(1, N):
    if case1[i - 1] != target[i - 1]:
        cnt1 += 1
        turn_on(case1, i)
    if case2[i - 1] != target[i - 1]:
        cnt2 += 1
        turn_on(case2, i)

if tuple(case1) != tuple(target):
    cnt1 = -1
if tuple(case2) != tuple(target):
    cnt2 = -1

print((-1 if cnt2 == -1 else cnt2) if cnt1 == - 1 else (min(cnt1, cnt2) if cnt2 != -1 else cnt1))