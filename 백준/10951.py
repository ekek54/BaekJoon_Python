import sys
N = int(sys.stdin.readline())
cycle = 0
C=N
while True:
    A= C // 10
    B= C % 10
    A= A + B
    A= A % 10
    A= B*10+A
    C= A
    cycle += 1
    if C == N:
        break
print(cycle)