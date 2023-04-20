import sys

S = sys.stdin.readline().rstrip()
stack = []
flag = True
answer = ''
for i in range(len(S)):
  if not flag:
    if S[i] != '>':
      answer += S[i]
    else:
      flag = True
      answer += S[i]
  elif flag:
    if S[i] == '<':
      while stack:
        answer += stack.pop()
      flag = False
      answer += S[i]
    elif S[i] == ' ':
      while stack:
        answer += stack.pop()
      answer += S[i]
    else:
      stack.append(S[i])
while stack:
  answer += stack.pop()
print(answer)
