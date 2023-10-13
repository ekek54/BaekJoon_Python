def solution(today, terms, privacies):
    answer = []
    today_y, today_m, today_d = map(int, today.split('.'))
    term_dict = {}
    for term in terms:
        name, term = term.split()
        term_dict[name] = int(term)
    print(term_dict)
    for i, privacy in enumerate(privacies):
        save_at, rule = privacy.split()
        save_y, save_m, save_d = map(int, save_at.split('.'))
        expire_m = (save_m + term_dict[rule]) % 12
        if expire_m == 0:
            expire_m = 12
        expire_y = save_y + (save_m + term_dict[rule] - 1) // 12
        expire_d = save_d - 1
        if expire_d == 0:
            expire_d = 28
            expire_m -= 1
            if expire_m == 0:
                expire_m = 12
                expire_y -= 1
        print(expire_y, expire_m, expire_d)
        if expire_y < today_y or (expire_y == today_y and expire_m < today_m) or (expire_y == today_y and expire_m == today_m and expire_d < today_d):
            answer.append(i + 1)
    return answer