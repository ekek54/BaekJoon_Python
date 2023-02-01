import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = []
result = 0
for i in range(N):
  if A[i] == 10:
    result += 1
  elif A[i] < 10:
    continue
  elif A[i] % 10 == 0:
    B.append(((A[i] // 10), (A[i] // 10 - 1)))
  else:
    B.append(((A[i] // 10), (A[i] // 10)))

B.sort(key=lambda x: -(x[0] / x[1]))

for i in range(len(B)):
  if B[i][1] <= M:
    result += B[i][0]
    M -= B[i][1]
  else:
    result += M
    M = 0
print(result)