import sys
N = int(sys.stdin.readline())
task=[tuple(map(int,sys.stdin.readline().split())) for i in range(N)]
schedul=[0 for i in range(1000)]
task.sort(key=lambda x:-x[1])
for t in task:
    d,w = t
    if schedul[d - 1] == 0:
        schedul[d - 1] = w
    else:
        idx=d-1
        while idx>0:
            idx-=1
            if schedul[idx] == 0:
                schedul[idx] = w
                break
print(sum(schedul))