import sys
input = sys.stdin.readline
N, K = map(int, input().split())
drinks = [int(input()) for _ in range(N)]

def calc(n):
    result = 0
    for drink in drinks:
        result += drink // n
    # print(result)
    return result

l = 1
r = max(drinks)
while l <= r:
    # print(l, r)
    mid = (l + r) // 2
    if calc(mid) < K:
        r = mid - 1
    else:
        l = mid + 1
print(r)