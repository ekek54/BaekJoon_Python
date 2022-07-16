import sys

def find(parent, a):
    if parent[a]==-1:
        return -1
    if parent[a]==a:
        return a
    else:
        parent[a]=find(parent,parent[a])
        return parent[a]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        if a == -1:
            return
        parent[a] = -1
        return False
    elif a < b:
        parent[b] = a
        return True
    else:
        parent[a] = b
        return True
num = 1
while 1:
    n, m = map(int, sys.stdin.readline().split())
    parent = [i for i in range(n + 1)]
    ans = []
    if (n, m)==(0, 0):
        break
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        union(parent, a, b)
    for i in range(1,n+1):
        root = find(parent, i)
        if root != -1:
            ans.append(root)
    #print(parent)
    ans = len(set(ans))
    if ans == 1:
        print("Case %d: There is one tree." %num)

    if ans > 1:
        print("Case %d: A forest of %d trees." %(num,ans))
    if ans == 0:
        print("Case %d: No trees." % num)
    num+=1