import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
lis = [1000000001]

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
    else:
        lis[bisec(A[i])] = A[i]
print(len(lis))