import sys
import heapq

N = int(sys.stdin.readline())
people = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
use_pq = []
wait_pq = []
cnt = 0
people.sort()
stack = [0]
for person in people:
    s, e = person
    # print(use_pq)
    # print(wait_pq)
    while use_pq:
        if use_pq[0][0] < s:
            end, num = heapq.heappop(use_pq)
            heapq.heappush(wait_pq, num)
        else: break
    if not wait_pq:
        cnt += 1
        stack.append(1)
        heapq.heappush(use_pq, (e, cnt))
    else:
        num = heapq.heappop(wait_pq)
        heapq.heappush(use_pq, (e, num))
        stack[num] += 1
print(cnt)
print(*stack[1:])