import sys
from collections import deque

formular = list(sys.stdin.readline().rstrip())

operand = deque()
operator = []
op_prior = {'+': 0, '-': 0, '*': 1, '/': 1}
bracket_count = 0
for i, op in enumerate(formular):
    if op =='(': bracket_count += 2
    elif op ==')': bracket_count -= 2
    elif op in op_prior:
        cur_prior = op_prior[op] + bracket_count
        if (not operator) or operator[-1][1] < cur_prior:
            operator.append((op, cur_prior))
        else:
            acc = ""
            while operand:
                acc += operand.popleft()
            while operator and operator[-1][1] >= cur_prior:
                acc += operator.pop()[0]
            operand.append(acc)
            operator.append((op, cur_prior))
    else:
        operand.append(op)

acc = ""
while operand:
    acc += operand.popleft()
while operator:
    acc += operator.pop()[0]
print(acc)