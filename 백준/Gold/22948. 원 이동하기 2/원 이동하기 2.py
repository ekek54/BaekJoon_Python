import sys
from collections import deque

intersection_circle_line = []
N = int(sys.stdin.readline())
for _ in range(N):
    circle_num, center, r = map(int, sys.stdin.readline().split())
    intersection_circle_line.append((center - r, circle_num))
    intersection_circle_line.append((center + r, -circle_num))

intersection_circle_line.sort()
adj_list = [[] for _ in range(N + 1)]
stack = [0]
for idx, intersection in enumerate(intersection_circle_line):
    x, circle_num = intersection
    if circle_num > 0:
        adj_list[stack[-1]].append(circle_num)
        stack.append(circle_num)
    else:
        adj_list[stack.pop()].append(stack[-1])
s, e = map(int, sys.stdin.readline().split())
que = deque()

visit = [False for _ in range(N + 1)]
que.append((s, 1))
visit[s] = True
pre = [i for i in range(N + 1)]
answer = 0
while que:
    node, dist = que.popleft()
    if node == e: answer = dist
    for adj in adj_list[node]:
        if visit[adj]: continue
        visit[adj] = True
        pre[adj] = node
        que.append((adj, dist + 1))

# print(adj_list)
print(answer)
# print(pre)
path = []
def get_path(n):
    path.append(n)
    if n == pre[n]:
        return
    get_path(pre[n])
get_path(e)
print(*reversed(path))