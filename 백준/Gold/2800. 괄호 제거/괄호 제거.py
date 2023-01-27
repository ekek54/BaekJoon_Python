import sys

parser_stack = []
formula = sys.stdin.readline().rstrip('\n')
pairs = []
for i in range(len(formula)):
  if formula[i] == '(':
    parser_stack.append(i)
  elif formula[i] == ')':
    pairs.append([parser_stack.pop(), i])
#print(pairs)

stack = []
answers = []
def dfs(cnt):
  if cnt == len(pairs):
    # 제거 괄호 없는 경우 예외처리
    if 0 not in stack:
      return
    # 출력
    flags = [True for _ in range(len(formula))]
    for i in range(cnt):
      if not stack[i]:
        for idx in pairs[i]:
          flags[idx] = False
    new_formular = ''
    for i in range(len(formula)):
      if flags[i]:
        new_formular += formula[i]
    answers.append(new_formular)
    return

  for i in range(2):
    stack.append(i)
    dfs(cnt+1)
    stack.pop()

dfs(0)
answers = list(set(answers))
answers.sort()
for i in range(len(answers)):
  print(answers[i])