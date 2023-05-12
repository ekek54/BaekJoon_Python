def solution(tickets):
    tickets.sort()
    print(tickets)
    route={}
    for idx,ticket in enumerate(tickets):
        if ticket[0] in route:
            route[ticket[0]].append([idx,ticket[1]])
        else:
            route[ticket[0]]=[[idx,ticket[1]]]
    N=len(tickets)
    chk=[False for i in range(N)]
    res=["ICN"]
    def dfs(cnt):
        if cnt==N:
            return res
        if res[-1] not in route:
            return
        for i in route[res[-1]]:
            if chk[i[0]]:
                continue
            res.append(i[1])
            chk[i[0]]=True
            if dfs(cnt+1):
                return res
            res.pop()
            chk[i[0]]=False
        return False
    return dfs(0)