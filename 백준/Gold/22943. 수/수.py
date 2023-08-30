import sys
from collections import deque

K, M = map(int, sys.stdin.readline().split())
generated_nums = []
stack = []
visit = [False for _ in range(10)]


def dfs(cnt):
    if cnt == K:
        generated_nums.append(int("".join(stack)))
        return

    for i in range(10):
        if not stack and i == 0: continue
        if visit[i]: continue
        stack.append(str(i))
        visit[i] = True
        dfs(cnt + 1)
        stack.pop()
        visit[i] = False


dfs(0)

max_num = generated_nums[-1]
primes = []
eratos = [False for _ in range(max_num + 1)]
eratos[0] = True
eratos[1] = True
for i in range(2, max_num + 1):
    j = 2
    while i * j <= max_num:
        eratos[i * j] = True
        j += 1
for i in range(max_num + 1):
    if not eratos[i]:
        primes.append(i)


def is_pirme_sum(n):
    l = 0
    r = len(primes) - 1
    while l < r:
        prime_sum = primes[l] + primes[r]
        if (prime_sum < n):
            l += 1
        elif prime_sum > n:
            r -= 1
        else:
            return True
    return False


def is_prime_mul(n):
    l = 0
    r = len(primes) - 1
    while l <= r:
        prime_mul = primes[l] * primes[r]
        if prime_mul < n:
            l += 1
        elif prime_mul > n:
            r -= 1
        else:
            return True
    return False


def mod_num(n, m):
    while n % m == 0:
        n //= m
    return n


answer = 0



for generated_num in generated_nums:
    if is_pirme_sum(generated_num) and is_prime_mul(mod_num(generated_num, M)):
        answer += 1

print(answer)
