import sys
from decimal import Decimal
from math import sqrt , inf
N, K = map(int, sys.stdin.readline().split())
person = list(map(int, sys.stdin.readline().split()))
start = 0
minV = inf
sdList = []
while start <= N - K:
    end = start + K
    initSet = person[start:end-1]
    normalSum = sum(initSet)
    squareSum = sum(map(lambda x : x**2,initSet))
    while end <= N:
        normalSum += person[end-1]
        squareSum += person[end-1]**2
        M = (normalSum / (end-start))
        V = (squareSum - 2*M*(normalSum) + (end-start) * (M**2)) / (end - start)
        if V < minV:
            M = Decimal(normalSum / (end-start))
            V = (squareSum - 2 * M * (normalSum) + (end - start) * (M ** 2)) / (end - start)
            minV = V
        end += 1
    start +=1

print(sqrt(minV))
