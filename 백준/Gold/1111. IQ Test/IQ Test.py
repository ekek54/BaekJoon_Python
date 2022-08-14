import sys


def calcAB(arr):
    if arr[1] == arr[0]:
        A = 1
        B = 0
        return [A, B]
    else:
        A = (arr[2] - arr[1]) / (arr[1] - arr[0])
        if A != int(A):
            return False
        B = arr[1] - A * arr[0]
        return [A, B]


def main(N, arr):
    if N == 1:
        return 'A'

    if N == 2:
        return arr[0] if arr[0] == arr[1] else 'A'

    else:
        AB = calcAB(arr)
        if not AB:
            return 'B'
        A, B = AB
        for i in range(1, N):
            if i == N - 1:
                return int(A * arr[i] + B)
            if A * arr[i] + B != arr[i + 1]:
                return 'B'


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(main(N, arr))