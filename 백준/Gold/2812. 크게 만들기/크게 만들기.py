import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
num = list(map(int, list(sys.stdin.readline().rstrip())))
ans_len = N - K
pq = [] #(num, idx)
answer = []
limit = -1
for i in range(K):
    heapq.heappush(pq, (-num[i], i))

for i in range(K, N):
    heapq.heappush(pq, (-num[i], i))
    while True:
        n, idx = heapq.heappop(pq)
        n = -n
        if idx > limit:
            answer.append(n)
            limit = idx
            break
print("".join(map(str,answer)))