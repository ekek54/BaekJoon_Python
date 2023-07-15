import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    minusOne = lambda x: int(x) - 1
    preOrder = list(map(minusOne, sys.stdin.readline().split()))
    inOrder = list(map(minusOne, sys.stdin.readline().split()))
    adjList = [[-1, -1] for i in range(n)]
    def dc(cnt, arr):
        # print(arr)
        cur = preOrder[cnt]
        m = arr.index(cur)
        l = arr[:m]
        if l:
            adjList[cur][0] = preOrder[cnt + 1]
            cnt = dc(cnt + 1, l)
        r = arr[m + 1:]
        if r:
            adjList[cur][1] = preOrder[cnt + 1]
            cnt = dc(cnt + 1, r)
        return cnt
    dc(0, inOrder)
    root = preOrder[0]
    postOrder = []
    def createPostOrder(node):
        if adjList[node][0] != -1:
            createPostOrder(adjList[node][0])
        if adjList[node][1] != -1:
            createPostOrder(adjList[node][1])
        postOrder.append(node)

    createPostOrder(root)

    print(*map(lambda x: x + 1, postOrder))
