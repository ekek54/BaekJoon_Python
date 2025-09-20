from math import inf
import heapq

def solution(alp, cop, problems):
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    
    max_req_alp = max([problem[0] for problem in problems])
    max_req_cop = max([problem[1] for problem in problems])
    
    # print(max_req_alp)
    # print(max_req_cop)
        
     
    dp = [[inf for j in range(600)] for i in range(600)]
    dp[alp][cop] = 0
    answer = inf
    pq = [(0, alp, cop)]
    while pq:
        cur_t, cur_alp, cur_cop = heapq.heappop(pq)
        if cur_t > answer: continue
        if cur_alp >= max_req_alp and cur_cop >= max_req_cop: 
            answer = min(answer, dp[cur_alp][cur_cop])
            continue
        if dp[cur_alp][cur_cop] < cur_t: continue
        for problem in problems:
            alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
            if cur_alp >= max_req_alp and cop_rwd == 0: continue
            if cur_cop >= max_req_cop and alp_rwd == 0: continue
            if cur_alp >= alp_req and cur_cop >= cop_req:
                nxt_alp = cur_alp + alp_rwd
                nxt_cop = cur_cop + cop_rwd
                if dp[nxt_alp][nxt_cop] > cur_t + cost:
                    dp[nxt_alp][nxt_cop] = cur_t + cost
                    heapq.heappush(pq, (cur_t + cost, nxt_alp, nxt_cop))
            
    # print(dp)
    return answer