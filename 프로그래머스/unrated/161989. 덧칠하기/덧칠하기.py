def solution(n, m, section):
    cur = 0
    answer = 0
    for i in range(len(section)):
        if cur < section[i]:
            cur = section[i] + m - 1
            answer += 1
    return answer