import sys

n = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
answer = 0
for i, a in enumerate(A):
    if not stack:
        stack.append(a)
    if stack[-1] < a:
        answer += a - stack[-1]
        while stack and stack[-1] <= a:
            stack.pop()
    stack.append(a)
if stack:
    answer += stack[0] - stack[-1]
print(answer)