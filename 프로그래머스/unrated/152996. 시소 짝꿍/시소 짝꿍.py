def solution(weights):
    weight_dict = dict()
    cnt = 0
    for weight in weights:
        if weight in weight_dict:
            weight_dict[weight] += 1
        else:
            weight_dict[weight] = 1
    for weight in weight_dict.keys():
        cnt += weight_dict[weight] * (weight_dict[weight] - 1) // 2
        if weight * 4 / 2 in weight_dict:
            cnt += weight_dict[weight] * weight_dict[weight * 2]
        if weight * 3 / 2 in weight_dict:
            cnt += weight_dict[weight] * weight_dict[weight * 3 // 2]
        if weight * 4 / 3 in weight_dict:
            cnt += weight_dict[weight] * weight_dict[weight * 4 // 3]
    return cnt