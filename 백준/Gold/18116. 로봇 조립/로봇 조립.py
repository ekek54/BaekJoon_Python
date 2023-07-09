import sys
input = sys.stdin.readline
N = int(input())
parent = [i for i in range(10**6)]
part_cnt = [1 for i in range(10**6)]

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
        part_cnt[a] += part_cnt[b]
    elif a > b:
        parent[a] = b
        part_cnt[b] += part_cnt[a]

for _ in range(N):
    command = list(input().split())
    op = command[0]
    if op == "I":
        arg1 = int(command[1]) - 1
        arg2 = int(command[2]) - 1
        union(arg1, arg2)
    elif op == "Q":
        arg1 = int(command[1]) - 1
        print(part_cnt[find(arg1)])