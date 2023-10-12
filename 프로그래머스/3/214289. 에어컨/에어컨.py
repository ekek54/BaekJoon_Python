from math import inf

def solution(temperature, t1, t2, a, b, onboard):
    N = len(onboard)
    dp = [[inf for j in range(51)] for i in range(N)]
    temperature += 10
    t1 += 10
    t2 += 10
    dp[0][temperature] = 0
    for i in range(1, N):
        for j in range(51):
            if onboard[i] == 1 and not (t1 <= j <= t2):
                continue
            if j < temperature :
                dp[i][j] = min(dp[i - 1][j - 1] if j > 1 else inf, dp[i - 1][j] + b, dp[i - 1][j + 1] + a)
            elif temperature < j:
                dp[i][j] = min(dp[i - 1][j - 1] + a, dp[i - 1][j] + b, dp[i - 1][j + 1] if j + 1 <= 50 else inf)
            elif temperature < t1 and temperature < t2:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1])
            elif temperature > t1 and temperature > t2:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1])
    # print(dp)
    return min(dp[-1])