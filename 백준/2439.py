import sys
N, X = sys.stdin.readline().split( )
N = int(N)
X = int(X)
zeros= 0
list = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    if list[i] < X:
        print(list[i], end=' ')