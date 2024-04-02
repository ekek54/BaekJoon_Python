def solution(a, b, n):
    answer = 0
    while a <= n:
        should = (n // a) * b
        mod = n % a
        n = should + mod
        answer += should
    return answer