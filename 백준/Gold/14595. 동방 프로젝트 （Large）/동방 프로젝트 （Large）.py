import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
rooms = [0 for _ in range(N)]
for _ in range(M):
  i, j = map(int, sys.stdin.readline().split())
  i -= 1
  j -= 1
  rooms[i] += 1
  rooms[j] -= 1

acc = 0
for i in range(N):
  acc += rooms[i]
  rooms[i] = acc
rooms.pop()
print(rooms.count(0) + 1)
