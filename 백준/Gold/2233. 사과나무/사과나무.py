import sys

N = int(sys.stdin.readline())
tree_bin = list(map(int, list(sys.stdin.readline().rstrip())))
X, Y = map(lambda x: int(x) - 1, sys.stdin.readline().split())
ij_list = [[-1, -1] for _ in range(N)]
parent = [-1 for i in range(N)]
idx = 0
stack = []
for i in range(len(tree_bin)):
    if tree_bin[i] == 0:
        ij_list[idx][0] = i
        stack.append(idx)
        if i == X:
            X = idx
        if i == Y:
            Y = idx
        idx += 1
    else:
        cur = stack.pop()
        ij_list[cur][1] = i
        if stack:
            parent[cur] = stack[-1]
        if i == X:
            X = cur
        if i == Y:
            Y = cur
visit = [False for _ in range(N)]
lowest_common_anc = -1
def check_ancestor(node):
    global lowest_common_anc
    if node == -1: return
    if not visit[node]:
        visit[node] = True
    else:
        lowest_common_anc = node
        return
    check_ancestor(parent[node])
check_ancestor(X)
check_ancestor(Y)
print(*map(lambda x: x + 1,ij_list[lowest_common_anc]))