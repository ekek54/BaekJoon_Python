from random import randrange
import sys

def dfsVideoTree(curVideo, visitVideo, recVideoNum, videoTree_adjDict, K):
  visitVideo[curVideo] = True

  if isLastDepthVideo(curVideo):
    return

  for adjInfo in videoTree_adjDict[curVideo]:
    adjVideo, usado = adjInfo
    if visitVideo[adjVideo]:
      continue
    elif usado >= K:
      recVideoNum += 1
      recVideoNum = dfsVideoTree(adjVideo, visitVideo, recVideoNum, videoTree_adjDict, K)
  return recVideoNum

def isLastDepthVideo(video, visitVideo, VideoTree_adjDict):
  for adjInfo in VideoTree_adjDict[video]:
    adjVideo, usado= adjInfo
    if not visitVideo[adjVideo]:
      return False
  return True

def main():
  N, Q = map(int,sys.stdin.readline().split())
  adjDict = {}
  visit = [False for _ in range(N+1)]
  cnt = 0 

  for i in range(N-1):
    p, q, r = map(int,sys.stdin.readline().split())
    if p in adjDict:
      adjDict[p].append((q, r))
    if q in adjDict:
      adjDict[q].append((p, r))
    if p not in adjDict:
      adjDict[p] = [(q,r)]
    if q not in adjDict:
      adjDict[q] = [(p,r)]

  for i in range(Q):
    k, v = map(int,sys.stdin.readline().split())
    print(dfsVideoTree(v, visit, 0, adjDict, k))

main()