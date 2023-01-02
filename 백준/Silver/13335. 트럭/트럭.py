import sys
from collections import deque

n, w, L = map(int, sys.stdin.readline().split())
truck_que = deque(map(int, sys.stdin.readline().split()))
bridge = deque()
cur_weight = 0
time = 0
while truck_que or bridge:
  time += 1
  for i in range(len(bridge)):
    bridge[i][1] += 1
  if len(bridge) >= 1 and bridge[0][1] == w:
    cur_weight -= bridge.popleft()[0]
  if len(truck_que) >= 1 and L - cur_weight >= truck_que[0]:
    cur_truck_weight = truck_que.popleft()
    bridge.append([cur_truck_weight, 0])  # [트럭 무게, 트럭 위치]
    cur_weight += cur_truck_weight
print(time)
