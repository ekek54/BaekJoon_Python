

import sys
T = int(sys.stdin.readline())
dp=[False,False,'1','7','4','2','0','8']+[False for i in range(8,101)]

def dynamic(arr,n):
    if arr[n]:
        return arr[n]
    else:
        l=2
        r=n-2
        tmp=[]

        while l<=r:
            tmp1=dynamic(arr, l) + dynamic(arr, r)
            tmp2=dynamic(arr,r) + dynamic(arr,l)
            if tmp1[0]=='0':
                tmp1='6'+tmp1[1:]
            if tmp2[0]=='0':
                tmp2='6'+tmp2[1:]
            tmp.append(tmp1)
            tmp.append(tmp2)
            r-=1
            l+=1
        arr[n]=str(min(map(int,tmp)))
        return arr[n]

for i in range(T):
    N=int(sys.stdin.readline())
    ans=dynamic(dp,N)
    if ans=='0':
        print('6','111')
    else:
        print(ans,'7'+'1'*((N//2)-1) if N%2==1 else '1'*(N//2))