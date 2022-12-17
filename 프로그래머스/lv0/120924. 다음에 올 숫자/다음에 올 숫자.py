def solution(common):
    if (common[0] * common[2] == common[1]**2):
        if(0 in common): return 0
        return common[-1] * common[1] / common[0]
    else:
        return common[-1] + (common[1] - common[0])