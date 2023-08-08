import sys

def le_cnt(n, limit):
    result = 0
    for i in range(1, int(n ** (1 / 2)) + 1):
        result += min((n // i), limit) - i
    result *= 2
    result += int(n ** (1 / 2))
    return result

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

l = 0
r = N ** 2

while l <= r:
    mid = (l + r) // 2
    if K <= le_cnt(mid, N):
        r = mid - 1
    elif K > le_cnt(mid, N):
        l = mid + 1

print(l)
