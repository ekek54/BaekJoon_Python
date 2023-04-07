import sys

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))


def acc_sums(arr):
  acc = 0
  res = [0]
  for i in range(len(arr)):
    acc += arr[i]
    res.append(acc)
  #print(res)
  return res


def sub_sums(acc_sums):
  N = len(acc_sums)
  res = []
  for i in range(N):
    for j in range(i + 1, N):
      res.append(acc_sums[j] - acc_sums[i])
  res.sort()
  #print(res)
  return res

answer = 0
A_sub_sums = sub_sums(acc_sums(A))
B_sub_sums = sub_sums(acc_sums(B))
l = 0
r = len(B_sub_sums) - 1
while l < len(A_sub_sums) and 0 <= r:
  A_sub_sum = A_sub_sums[l]
  B_sub_sum = B_sub_sums[r]
  key = A_sub_sum + B_sub_sum
  #print(l, r, key)
  if key < T:
    l += 1
  elif key > T:
    r -= 1
  else:
    l_dup_idx = l
    l_dup_cnt = 0
    while l_dup_idx < len(A_sub_sums) and A_sub_sums[l_dup_idx] == A_sub_sum:
      l_dup_idx += 1
      l_dup_cnt += 1
    r_dup_idx = r
    r_dup_cnt = 0
    while r_dup_idx >= 0 and B_sub_sums[r_dup_idx] == B_sub_sum:
      r_dup_idx -= 1
      r_dup_cnt += 1
    answer += l_dup_cnt * r_dup_cnt
    l = l_dup_idx
    r = r_dup_idx

print(answer)