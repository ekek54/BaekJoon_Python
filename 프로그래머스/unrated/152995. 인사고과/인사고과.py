def solution(scores):
    if len(scores) == 1:
        return 1
    my_score = scores[0]
    scores = scores[1:]
    scores.sort(reverse=True)
    answer = 0
    cl = 0
    cr = scores[0][1]
    r = scores[0][0]
    
    def high_score(score):
        return sum(score) > sum(my_score)
    
    for score in scores:
        if score[0] > my_score[0] and score[1] > my_score[1]:
            return -1
        if score[0] < r:
            cl, cr = max(cl,cr), score[1]
            r = score[0] 
        if score[0] == r:
            if cl <= score[1] <= cr and high_score(score):
                answer += 1
    return answer + 1