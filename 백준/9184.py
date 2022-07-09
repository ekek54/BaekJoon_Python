import collections
import sys
a = 0
b = 0
c = 0
case_list= list()
memo=[[[0 for col in range(21)] for row in range(21)]for high in range(21)]
while(1):
    a, b ,c = map(int,sys.stdin.readline().split(' '))
    if a == -1 and b == -1 and c == -1:
        break
    case_list.append([a,b,c])
def memorization_w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
       return 1
    if a > 20 or b > 20 or c > 20:
        return memorization_w(20,20,20)
    if memo[a][b][c] > 0:
        return memo[a][b][c]
    if a < b and b < c:
        memo[a][b][c] = memorization_w(a,b,c-1) + memorization_w(a,b-1,c-1) - memorization_w(a,b-1,c)
        return memo[a][b][c]
    else:
        memo[a][b][c] = memorization_w(a-1,b,c) + memorization_w(a-1,b-1,c) + memorization_w(a-1,b,c-1) - memorization_w(a-1,b-1,c-1)
        return memo[a][b][c]
for i in case_list:
    print('w(',end='')
    print(i[0],end='')
    print(',',i[1],end='')
    print(',',i[2],end='')
    print(') =',end=' ')
    print(memorization_w(i[0],i[1],i[2]))