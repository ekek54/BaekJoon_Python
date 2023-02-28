import sys
from math import inf
sys.setrecursionlimit(100001)
def solution(target):
    dp = [[0,0] for _ in range(100001)]
    dp[0] = [0, 0]
    dp[50] = [1, 1]
    for i in range(20):
        for j in range(3):
            if j == 0:
                dp[i + 1] = [1, 1]
            elif sum(dp[(i + 1) * (j + 1)]) == 0:
                dp[(i + 1) * (j + 1)] = [1, 0]
    def top_down(score):
        if sum(dp[score]) != 0:
            return dp[score]
        candid = []
        for i in range(20):
            for j in range(3):
                if score - ((i + 1) * (j + 1)) > 0:
                    pre = top_down(score - ((i + 1) * (j + 1)))[:]
                    if j == 0:
                        pre[1] += 1
                    pre[0] += 1
                    candid.append(pre)
        if score - 50 > 0:
            pre = top_down(score - 50)[:]
            pre[0] += 1
            pre[1] += 1
            candid.append(pre)
        candid.sort(key = lambda x: (x[0], -x[1]))
        dp[score] = candid[0]
        return dp[score]
    return top_down(target)