def solution(s):
    N = len(s)
    answer = [0 for _ in range(N)]
    num_memo = {}
    for i,v in enumerate(s):
        if v in num_memo:
            answer[i] = i - num_memo[v]
        else:
            answer[i] = -1
        num_memo[v] = i
    return answer