import heapq

def solution(n, k, enemy):
    cur = 0
    cleared = []
    answer = 0
    while(n >= 0 and cur < len(enemy)):
        n -= enemy[cur]
        heapq.heappush(cleared, -enemy[cur])
        if (n < 0 and k > 0):
            max_cleared = -1 * heapq.heappop(cleared)
            n += max_cleared
            k -= 1
        if (n >= 0):
            answer += 1
            cur += 1
    return answer