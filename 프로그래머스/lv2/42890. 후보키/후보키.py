from itertools import combinations

def solution(relation):
    rows = len(relation)
    cols=len(relation[0])
    col_list=[[relation[i][j] for i in range(rows)] for j in range(cols)]
    answer=[]
    
    def uniq(candidates): #후보군 유일성 체크
        key_list=["".join([str(i)+col_list[i][j] for i in candidates]) for j in range(rows)]
        return True if len(set(key_list))==len(key_list) else False
    
    for i in range(1,cols+1):
        tmp=list(combinations(range(cols),i))
        for t in tmp:
            if uniq(t):
                answer.append(t)
    tmp=answer[:]
    for i in range(len(answer)):
        for j in answer[i+1:]:
            if set(answer[i]) < set(j) and j in tmp:
                tmp.remove(j)
    return len(tmp)