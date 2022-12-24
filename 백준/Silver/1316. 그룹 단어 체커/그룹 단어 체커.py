def group(a: str):
    word= list()
    a = list(a)
    b = a.copy()
    for i in range(len(a)):
        if i == len(a)-1:
            break
        if a[i] == a[i+1]:
             b.remove(a[i])
    for i in b:
        if i in word:
            return 0
        else:
            word.append(i)
    return 1

import sys
N = int(sys.stdin.readline())
count = 0
for i in range(N):
    word = list(str(sys.stdin.readline()))
    count += group(word)
print(count)