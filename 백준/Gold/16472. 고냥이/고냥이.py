import sys

N = int(sys.stdin.readline())
string = list(sys.stdin.readline().rstrip())
alpha_counts = {}
l = 0
r = 0
alpha_counts[string[0]] = 1
answer = 0
while True:
  #print(alpha_counts)
  if len(alpha_counts) <= N:
    r += 1
    if r == len(string):
      answer = max(answer, r - l)
      break

    if string[r] in alpha_counts:
      alpha_counts[string[r]] += 1
    else:
      alpha_counts[string[r]] = 1

    if len(alpha_counts) > N:
      answer = max(answer, r - l)
  elif len(alpha_counts) > N:
    alpha_counts[string[l]] -= 1
    if alpha_counts[string[l]] == 0:
      del alpha_counts[string[l]]
    l += 1

print(answer)