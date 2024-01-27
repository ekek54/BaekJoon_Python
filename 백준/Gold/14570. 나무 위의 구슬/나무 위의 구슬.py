import sys

N = int(sys.stdin.readline())
tree = [[-1, -1] for _ in range(N)]
for i in range(N):
    tree[i] = list(map(lambda x: int(x) - 1 if int(x) != -1 else int(x), sys.stdin.readline().split()))
K = int(sys.stdin.readline())
cur_node = 0
while 1:
    # print(cur_node)
    # print(K)
    # print("------")
    if tree[cur_node][0] == -1 and tree[cur_node][1] == -1:
        break
    elif tree[cur_node][0] == -1:
        cur_node = tree[cur_node][1]
    elif tree[cur_node][1] == -1:
        cur_node = tree[cur_node][0]
    else:
        if K % 2 == 1:
            cur_node = tree[cur_node][0]
            K = K // 2 + 1
        else:
            cur_node = tree[cur_node][1]
            K = K // 2
print(cur_node + 1)