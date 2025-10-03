import sys
A, B = map(int, sys.stdin.readline().split(' '))
num_list= [i + 1 for i in range(A)]
check_list=[False] * A
result_list=[]
def DFS(count):
    if count == B:
        
        print(*result_list)
        return
    for i in range(A):
        if(check_list[i]):
            continue
        elif len(result_list)!=0 and result_list[count-1] > num_list[i]:
            continue

        check_list[i]=True
        result_list.append(num_list[i])
        DFS(count+1)
        result_list.pop()
        check_list[i] = False
DFS(0)