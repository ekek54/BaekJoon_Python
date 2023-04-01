import sys

N = int(sys.stdin.readline())
scores = []
for _ in range(N):
  scores.append(int(sys.stdin.readline()))

scores.reverse()
cnt = 0
for i in range(1, N):
  if scores[i - 1] > scores[i]:
    continue
  else:
    cnt += scores[i] - (scores[i - 1] - 1)
    scores[i] = scores[i - 1] - 1

print(cnt)