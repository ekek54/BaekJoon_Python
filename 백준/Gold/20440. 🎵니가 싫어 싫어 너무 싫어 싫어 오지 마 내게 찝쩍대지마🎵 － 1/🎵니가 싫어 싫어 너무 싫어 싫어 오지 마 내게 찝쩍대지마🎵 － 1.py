import sys

N = int(sys.stdin.readline())
enters = [-1]
exits = [-1]

for _ in range(N):
    E, X = map(int, sys.stdin.readline().split())
    enters.append(E)
    exits.append(X)

enters.sort()
exits.sort()

l = 0
r = 0
ans_cnt = 0
ans_s = 0
ans_e = 0
cnt = 0
flag = False

while l < N:
    if enters[l + 1] < exits[r + 1]:
        l += 1
        cnt += 1
    elif enters[l + 1] > exits[r + 1]:
        r += 1
        cnt -= 1
    else:
        l += 1
        r += 1

    if ans_cnt < cnt:
        ans_cnt = cnt
        ans_s = enters[l]
        ans_e = exits[r + 1]
        flag = True
    elif flag and ans_cnt == cnt:
        ans_e = exits[r + 1]
    else:
        flag = False

print(ans_cnt)
print(ans_s, ans_e)