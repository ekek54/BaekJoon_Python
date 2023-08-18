import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    print(min(nums), max(nums))
