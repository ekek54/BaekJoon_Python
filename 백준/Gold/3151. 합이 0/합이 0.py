import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
num_dict = {}
for i, a in enumerate(A):
    if a in num_dict:
        num_dict[a] += 1
    else:
        num_dict[a] = 1
# print(num_dict)
A = list(set(A))
A.sort()
N = len(A)
answer = 0
def calc_case(a, b, c):
    l = list({a, b, c})
    result = 0
    if len(l) == 3:
        result = 1
        for i in range(3):
            result *= num_dict[l[i]]
    elif len(l) == 1:
        result = num_dict[l[0]] * (num_dict[l[0]] - 1) * (num_dict[l[0]] - 2)
        result //= 6
    else:
        result = 1
        if b == a:
            result *= num_dict[a] * (num_dict[a] - 1)
            result //= 2
            result *= num_dict[c]
        else:
            result *= num_dict[c] * (num_dict[c] - 1)
            result //= 2
            result *= num_dict[a]
    # print(result)
    return result


for i in range(N):
    l = i
    r = N - 1
    while l <= r:
        if A[i] + A[l] + A[r] == 0:
            # print(A[i], A[l], A[r])
            # print(calc_case(A[i], A[l], A[r]))
            answer += calc_case(A[i], A[l], A[r])
            l += 1
        elif A[i] + A[l] + A[r] < 0:
            l += 1
        else:
            r -= 1

print(answer)