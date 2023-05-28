# edge_list에 (from, to) 를 저장
# edge_list 순회
#   현재 edge 그래프에서 제거
#   그래프에서 두 개의 트리를 찾아서 각각 지름을 더하고 제거한 edge의 가중치를 더한다.
#   현재 edge 그래프에 다시 추가
#   최대값 갱신
# 정답 출력
import sys
sys.setrecursionlimit(3000)
answer = 0
N = int(sys.stdin.readline())
edge_dict = {}
adj_list = [[] for _ in range(N)]


def diameter(src, disconnect):
    visit = [False for _ in range(N)]

    def dfs(node, max_dist, opp, acc_cost):

        for nxt in adj_list[node]:
            if node == src and nxt == disconnect: continue
            if visit[nxt]: continue
            visit[nxt] = True
            (max_dist, opp) = dfs(nxt, max_dist, opp, acc_cost + edge_dict[tuple(sorted((node, nxt)))])
            visit[nxt] = False

        if max_dist < acc_cost:
            max_dist = acc_cost
            opp = node
        return (max_dist, opp)

    visit[src] = True
    dist, opp = dfs(src, 0, src, 0)
    visit[src] = False
    visit[opp] = True
    result = dfs(opp, 0, opp, 0)

    return result[0]


for _ in range(N - 1):
    f, t, c = map(int, sys.stdin.readline().split())
    if f > t:
        f, t = t, f
    edge_dict[(f, t)] = c
    adj_list[f].append(t)
    adj_list[t].append(f)

for a, b in edge_dict.keys():
    cost = edge_dict[(a, b)]
    answer = max(answer, diameter(a, b) + diameter(b, a) + cost)

print(answer)
