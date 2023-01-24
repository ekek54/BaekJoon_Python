import sys
from collections import deque

r, c, k = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
answer = 0

def sort_op(arr):
  elem_cnt = {}
  for i in range(len(arr)):
    if arr[i] in elem_cnt:
      elem_cnt[arr[i]] += 1
    else:
      elem_cnt[arr[i]] = 1
  sorted_arr = sorted(list(elem_cnt.items()), key = lambda x: [x[1], x[0]])
  new_arr =[]
  for elem_cnt in sorted_arr:
    if elem_cnt[0] == 0:
      continue
    new_arr += elem_cnt
  return new_arr

while answer <= 100:
  R = len(A)
  C = len(A[0])
  new_A = []
  max_len = 0
  # 확인
  if R > r - 1 and C > c - 1:
    if A[r-1][c-1] == k:
      break
  answer += 1
  # R연산
  if R >= C:
    # 정렬
    for i in range(R):
      row = A[i]
      sorted_row = sort_op(row)
      max_len = max(max_len, len(sorted_row))
      new_A.append(sorted_row)
    # 패딩
    for i in range(R):
      new_A[i] += [0 for _ in range(max_len - len(new_A[i]))]
  # C 연산
  elif C > R:
    # 정렬
    for i in range(C):
      col = [A[j][i] for j in range(R)]
      sorted_col = sort_op(col)
      new_A.append(sorted_col)
      max_len = max(max_len, len(sorted_col))
    # 패딩
    for i in range(C):
      new_A[i] += [0 for _ in range(max_len - len(new_A[i]))]
    # 뒤집기
    new_A = [[new_A[j][i] for j in range(len(new_A))] for i in range(len(new_A[0]))]
  A = new_A
print(-1 if answer > 100 else answer)