import sys

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    if N%9==0:
        print("TAK")
    elif N%3 == 2:
        print("TAK")
    else:
        print("NIE")