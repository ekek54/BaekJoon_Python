def solution(sequence, k):
    acc_sums = [0]
    N = len(sequence)
    acc = 0
    for i in range(N):
        acc += sequence[i]
        acc_sums.append(acc)
    l = 0
    r = 1
    answer = [-1, N]
    while l < r <= N:
        sub_sum = acc_sums[r] - acc_sums[l]
        if sub_sum < k:
            r += 1
        elif sub_sum > k:
            l += 1
        elif (r - l) < answer[1] - answer[0]:
            answer = [l, r]
            r += 1
        else:
            r += 1
    answer[1] -= 1
    return answer