import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
acc_sums = [0]
acc = 0
for i in range(N):
    acc += A[i]
    acc_sums.append(acc)
acc_dict = {}
for acc_sum in acc_sums:
    if acc_sum in acc_dict:
        acc_dict[acc_sum] += 1
    else:
        acc_dict[acc_sum] = 1

answer = 0
for i in range(N):
    acc_dict[acc_sums[i]] -= 1
    target = acc_sums[i] + K
    if target in acc_dict:
        answer += acc_dict[target]

print(answer)
