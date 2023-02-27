def solution(sticker):
    N=len(sticker)
    if N == 1:
        return sticker[0]
    # 첫번째 스티커를 안쓰는 경우
    without_first = sticker[1:]
    without_last = sticker[: -1]
    # 문제의 상황을 순회하지 않는 1차원 배열의 경우로 가정한 솔루션
    def select_sticker(sticker):
        n = len(sticker)
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [sticker[0], 0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][1] + sticker[i]
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
        return max(dp[n - 1])
    return max(select_sticker(without_first), select_sticker(without_last))