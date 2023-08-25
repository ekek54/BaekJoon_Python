import sys
N, K = map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))
Q = int(sys.stdin.readline())
num_dict = {}
for i in range(K):
    if X[i] in num_dict:
        num_dict[X[i]] += 1
    else:
        num_dict[X[i]] = 1

a = [0 for _ in range(N)]

for k in num_dict.keys():
    i = 0
    while i < N:
        a[i] += num_dict[k]
        i += k
acc_sums = [0 for _ in range(N + 1)]
acc_sum = 0
for i in range(1, N + 1):
    acc_sum += a[i - 1]
    acc_sums[i] = acc_sum

for _ in range(Q):
    l, r = map(int,sys.stdin.readline().split())
    print(acc_sums[r + 1] - acc_sums[l])

# print(a)
# print(acc_sums)