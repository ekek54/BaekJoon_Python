import heapq
def solution(n, cores):
    if n <= len(cores): return n
    l = 0
    r = 500000000
    while l <= r:
        mid = (l + r) // 2
        if sum([mid // core if mid % core == 0 else mid // core + 1 for core in cores]) >= n:
            r = mid - 1
        else:
            l = mid + 1
    end_time = l
    assigned_work = sum([end_time // core if end_time % core == 0 else end_time // core + 1 for core in cores])
    candid = []
    for idx, core in enumerate(cores):
        if (end_time - 1) % core == 0:
            candid.append((core, idx))
    #print(end_time)
    #print(assigned_work)
    #print(candid)
    #print(candid[n - assigned_work - 1])
    return candid[n - assigned_work - 1][1] + 1