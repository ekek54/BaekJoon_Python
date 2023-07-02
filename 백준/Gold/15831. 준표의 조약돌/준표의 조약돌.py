import sys

N, B, W = map(int, sys.stdin.readline().split())
road = " " + sys.stdin.readline().rstrip()
# print(road)
l = 0
r = 0
cnt = {"B": 0, "W": 0}
answer = 0
while l <= r <= N:
    # print(l, r, cnt)
    if cnt["B"] <= B:
        if cnt["W"] >= W:
            answer = max(answer, r - l)
        r += 1
        if r > N: break
        cnt[road[r]] += 1
    else:
        l += 1
        cnt[road[l]] -= 1
print(answer)