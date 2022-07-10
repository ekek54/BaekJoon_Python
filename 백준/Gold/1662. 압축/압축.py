import sys
S=str(sys.stdin.readline().rstrip('\n'))
stack_num=[]
N=len(S)
tmp=0
for i in range(N):
    if S[i]=='(':
        tmp-=1
        stack_num.append((tmp,int(S[i-1])))
        tmp=0
    elif S[i]==')':
        tmp=stack_num[-1][1]*tmp+stack_num[-1][0]
        stack_num.pop()
    else:
        tmp+=1
print(tmp)