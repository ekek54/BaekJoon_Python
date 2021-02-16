import sys

N = sys.stdin.readline().rstrip()
N = int(N)
for i in range(1,N+1):
    A, B = sys.stdin.readline().rstrip().split( )
    A = int(A)
    B = int(B)
    print(A+B)