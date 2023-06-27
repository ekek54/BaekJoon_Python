import sys

C = int(sys.stdin.readline())
for i in range(C):
    arr = list(map(int, sys.stdin.readline().split(' ')))
    N = arr[0]
    scores = arr[1:]
    avg = sum(scores) / N
    over = 0
    for score in scores:
        if score > avg:
            over += 1
    print('%.3f%%'%((over / N) * 100))
