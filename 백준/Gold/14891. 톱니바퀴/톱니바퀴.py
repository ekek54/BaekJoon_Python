from collections import deque
import sys
wheel=[]
for i in range(4):
    arr=sys.stdin.readline().rstrip('\n')
    wheel_info=[arr[j] for j in range(8)]
    wheel.append(deque(map(int,wheel_info)))

def get_between(wheel):
    res=[]

    for i in range(3):
        if wheel[i][2]!=wheel[i+1][6]:
            res.append(1)
        else:
            res.append(0)
    return res

def wheel_spin(wheel_num,spin):
    if spin==-1:
        tmp=wheel[wheel_num].popleft()
        wheel[wheel_num].append(tmp)
    elif spin==1:
        tmp = wheel[wheel_num].pop()
        wheel[wheel_num].insert(0,tmp)
    return

N=int(sys.stdin.readline())
for i in range(N):
    spins = [0, 0, 0, 0]
    wheel_num, spin = map(int, sys.stdin.readline().split())
    wheel_num -= 1  # 1,2,3,4 => 0,1,2,3
    spins[wheel_num] = spin
    between = get_between(wheel)
    l=wheel_num-1
    r=wheel_num+1
    while l>=0:
        if between[l]==1:
            spins[l] = 1 if spins[l + 1] == -1 else -1
            l-=1
        else:
            break
    while r<4:
        if between[r-1]==1:
            spins[r] = 1 if spins[r-1] == -1 else -1
            r+=1
        else:
            break
    for idx,s in enumerate(spins):
        wheel_spin(idx,s)
print(sum([wheel[i][0]*(2**i) for i in range(4)]))