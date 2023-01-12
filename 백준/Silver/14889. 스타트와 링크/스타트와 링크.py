import sys
N= int(sys.stdin.readline())
ability= list()
member_check=[False for col in range(N)] #팀에 포함된 선수 체크
start= list() 
link= list(range(N)) #link팀에서 한명씩 골라서 start팀에 넣는 방식
gap_list=list()
for i in range(N):
    ability.append(list(map(int,sys.stdin.readline().split())))
def team_ability(team): #선정된 팀의 능력치 계산 함수
    result =0
    for i in range(N//2):
        for j in range(N//2):
            if i==j:
                continue
            else:
                result += ability[team[i]][team[j]]
    return result

def dfs(cnt): #dfs를 팀당 인원만큼 돌려서 팀원 선정 경우 탐색
    if (cnt == N // 2 ):
        gap_list.append(abs(team_ability(start)-team_ability(link)))

        return
    for j in range(N):
        if member_check[j] == True:
            continue
        elif len(start) != 0 and j < max(start):
            continue
        member_check[j] = True
        start.append(j)
        link.remove(j)
        dfs(cnt + 1)
        member_check[j] = False
        start.remove(j)
        link.append(j)

dfs(0)
print(min(gap_list))