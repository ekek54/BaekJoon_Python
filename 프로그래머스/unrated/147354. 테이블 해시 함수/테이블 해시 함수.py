def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x: [x[col-1],-x[0]])
    arr = []
    for i in range(row_begin-1, row_end):
        arr.append(S_n(i+1,data[i]))
    return xor(arr)

def S_n(n, tup):
    return sum(map(lambda x: x % n, tup))

def xor(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans ^ arr[i]
    return ans