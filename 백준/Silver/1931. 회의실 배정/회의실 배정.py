import sys
N= int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split(' '))) for i in range(N)]
arr.sort(key= lambda x:(x[1],x[0]))
sum=1
tmp = arr[0]
for i in range(1,len(arr)):
    if tmp[1]<=arr[i][0]:
        tmp=arr[i]
        sum+=1
print(sum)