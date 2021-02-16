import sys
N = sys.stdin.readline()
N = int(N)
star = '*'
for i in range(N):
    list = star * (i+1)
    print(list.rjust(N))
