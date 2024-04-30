def solution(n, tops):
    dp = [[0 for _ in range(4)] for i in range(n)]
    dp[0][0] = 1
    dp[0][1] = 1
    dp[0][2] = 1
    dp[0][3] = 1 if tops[0] == 1 else 0
    
    for i in range(1, n):
        dp[i][0] = sum(dp[i - 1]) % 10007
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3]) % 10007
        dp[i][2] = sum(dp[i - 1]) % 10007
        dp[i][3] = (sum(dp[i - 1]) if tops[i] == 1 else 0) % 10007
    # print(dp)
    return sum(dp[-1]) % 10007