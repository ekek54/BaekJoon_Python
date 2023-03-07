def solution(money):
    def bottom_up(money):
        arr = [[0, 0] for _ in range(n)]
        arr[0] = [money[0], 0]
        for i in range(1, len(arr)):
            arr[i][0] = arr[i - 1][1] + money[i]
            arr[i][1] = max(arr[i - 1])
        return max(arr[-1])
    n = len(money)
    # 1 사용 -1 사용 x
    money1 = money[:]
    money1[-1] = 0
    #print(bottom_up(money1))
    # 1 사용 x -1 사용
    money2 = money[:]
    money2[0] = 0
    #print(bottom_up(money2))
    return max(bottom_up(money1), bottom_up(money2))