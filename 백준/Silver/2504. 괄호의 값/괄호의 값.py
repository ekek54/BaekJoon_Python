import sys

A = sys.stdin.readline().rstrip()
N = len(A)
p_stack = []
num_stack = [0]

def correct(p):
    return p_stack and ((p_stack[-1] == "(" and p == ")") or (p_stack[-1] == "[" and p == "]"))

valid = True

for i in range(N):
    # print(num_stack)
    if A[i] == "[" or A[i] == "(":
        p_stack.append(A[i])
        num_stack.append(0)
    else:
        if correct(A[i]):
            pop_p = p_stack.pop()
            pop_num = num_stack.pop()
            if pop_num == 0:
                pop_num = 1
            num_stack[-1] += pop_num * (2 if pop_p == '(' else 3)
        else:
            valid = False
            break
if len(num_stack) != 1:
    valid = False

print(num_stack.pop() if valid else 0)

