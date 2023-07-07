import sys

N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
x.sort()
print(sum(x[:-1])/2 + x[-1])
