import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
lis = [1000000001]
idxs = [0 for _ in range(N)]

def bisec(k):
    l = 0
    r = len(lis)
    while l <= r:
        mid = (l + r) // 2
        if lis[mid] < k:
            l = mid + 1
        else:
            r = mid - 1
    return l

for i in range(N):
    if lis[-1] < A[i]:
        lis.append(A[i])
        idxs[i] = len(lis) - 1
    else:
        idx = bisec(A[i])
        lis[idx] = A[i]
        idxs[i] = idx
# print(idxs)
# print(lis)
subs = []
cur_idx = len(lis) - 1
for i in reversed(range(N)):
    if idxs[i] == cur_idx:
        subs.append(A[i])
        cur_idx -= 1
print(len(lis))
print(*reversed(subs))