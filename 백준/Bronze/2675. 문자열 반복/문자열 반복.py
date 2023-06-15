import sys
from math import inf
T = int(input())

for i in range(T):
    R, S = input().rstrip().split()
    result = ""
    R = int(R)
    for q in S:
        result += q * R
    print(result)