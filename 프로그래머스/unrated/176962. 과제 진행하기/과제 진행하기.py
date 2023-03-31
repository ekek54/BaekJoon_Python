def minute_format(hour_format):
    h, m = map(int, hour_format.split(':'))
    return h * 60 + m
def solution(plans):
    convert_form = lambda x: (x[0], minute_format(x[1]), int(x[2]))
    plans = list(map(convert_form, plans))
    plans.sort(key = lambda x: x[1])
    N = len(plans)
    wait = []
    answer = []
    for i in range(N - 1):
        cur_name, cur_start, cur_playtime = plans[i]
        cur_end = cur_start + cur_playtime
        nxt_name, nxt_start, nxt_playtime = plans[i + 1]
        if cur_end > nxt_start:
            wait.append((cur_name, cur_start, cur_end - nxt_start))
        elif cur_end == nxt_start:
            answer.append(cur_name)
        else:
            answer.append(cur_name)
            remain = nxt_start - cur_end
            while remain > 0 and wait:
                top_name, top_start, top_playtime = wait.pop()
                if top_playtime > remain:
                    top_playtime -= remain
                    remain = 0
                    wait.append((top_name, top_start, top_playtime))
                else:
                    remain -= top_playtime
                    answer.append(top_name)
        
    return answer + [plans[-1][0]] + list(reversed([wait[i][0] for i in range(len(wait))]))