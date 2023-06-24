import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(E)]
parent = [i for i in range(V)]
edges.sort(key=lambda x: x[2])


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    return True

answer = 0
for edge in edges:
    a, b, c = edge
    a -= 1
    b -= 1
    if union(a, b):
        answer += c
print(answer)