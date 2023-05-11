from collections import deque
def cmp(a,b):
    cnt=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            cnt+=1
    return True if cnt==1 else False
def solution(begin, target, words):
    if not target in words:
        return 0
    que= deque()
    que.append(begin)
    words.insert(0,begin)
    visit=[False for i in range(len(words))]
    chk=[0 for i in range(len(words))]
    visit[0]=True
    while que:
        cur_word=que.popleft()
        for idx,word in enumerate(words):
            if cmp(word,cur_word) and visit[idx]==False:
                nxt_word=word
                chk[idx]=chk[words.index(cur_word)]+1
                que.append(nxt_word)
                visit[words.index(nxt_word)]=True
    return chk[words.index(target)]