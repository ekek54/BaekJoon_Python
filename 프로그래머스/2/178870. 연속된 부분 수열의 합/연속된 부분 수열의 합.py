def solution(sequence, k):
    sub_sum = sequence[0]
    l = 0
    r = 0
    N = len(sequence)
    answer = []
    while l <= r < N:
        if sub_sum < k:
            r += 1
            if r == N: break
            sub_sum += sequence[r]
        elif sub_sum > k:
            sub_sum -= sequence[l]
            l += 1
            if l > r: break
        else:
            if len(answer) == 0 or r - l < answer[1] - answer[0]:
                answer = [l, r]
            # print(answer)
            r += 1
            if r == N: break
            sub_sum += sequence[r]
    
    return answer