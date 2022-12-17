def solution(lines):
    answer = 0
    x_axis = [0 for _ in range(200)]
    for line in lines:
        for i in range(*line):
            x_axis[i] += 1
    for x in x_axis:
        if x >= 2:
            answer += 1
    return answer