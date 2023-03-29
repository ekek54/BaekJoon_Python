def solution(numbers):
    N = len(numbers)
    # (v, idx)
    dp = [[-1, -1] for _ in range(N)]
    for i in reversed(range(N - 1)):
        if numbers[i] < numbers[i+1]:
            dp[i] = [numbers[i + 1], i + 1]
        else:
            if numbers[i] < dp[i + 1][0]:
                dp[i] = dp[i + 1]
            else:
                j = dp[i + 1][1]
                while dp[j][0] != -1 and j != -1:
                    if numbers[i] < dp[j][0]:
                        dp[i] = dp[j]
                        break
                    else:
                        j = dp[j][1]               
    return [dp[i][0] for i in range(N)]