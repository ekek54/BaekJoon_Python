import sys
N = int(sys.stdin.readline())
i=1
title=list()
while 1:
    k= list(str(i))
    for j in range(len(k)-2):
        if int(k[j]) == 6 and int(k[j+1]) ==6 and int(k[j+2]) == 6:
            title.append(i)
            break
    if len(title) == N:
        break
    i+=1
print(title[N-1])
