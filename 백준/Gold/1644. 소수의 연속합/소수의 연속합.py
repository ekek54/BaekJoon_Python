import sys

N = int(sys.stdin.readline())
eratos = [False for _ in range(N + 1)]
primes = []
for i in range(2, N // 2 + 1):
  j = 2
  while i * j < N + 1:
    eratos[i * j] = True
    j += 1
for i in range(2, N + 1):
  if not eratos[i]:
    primes.append(i)
acc_sums = [0]
acc = 0
for prime in primes:
  acc += prime
  acc_sums.append(acc)
l = 0
r = 1
result = 0
while r < len(acc_sums):
  sub_sum = acc_sums[r] - acc_sums[l]
  if sub_sum < N:
    r += 1
  elif sub_sum > N:
    l += 1
  elif sub_sum == N:
    result += 1
    r += 1
print(result)