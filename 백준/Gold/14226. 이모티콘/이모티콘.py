import sys
from collections import deque
S = int(sys.stdin.readline())
dist = [[0 for j in range(1001)] for i in range(1001)]
visit = [[False for j in range(1001)] for i in range(1001)]
que = deque()
que.append((1, 0))
visit[1][0] = visit

def OOB(r, c):
  global S
  return not (0 <= r < 1001 and 0 <= c < 1001)

while que:
  cur_emoji_num, cur_clipboard_num = que.popleft()
  if cur_emoji_num == S:
    print(dist[cur_emoji_num][cur_clipboard_num])
    break
  # 붙여넣기, 복사, 삭제
  nxts = [(cur_emoji_num + cur_clipboard_num, cur_clipboard_num),
          (cur_emoji_num, cur_emoji_num),
          (cur_emoji_num - 1, cur_clipboard_num)]
  for nxt in nxts:
    nxt_emoji_num, nxt_clipboard_num = nxt
    if OOB(nxt_emoji_num,nxt_clipboard_num): continue
    if not visit[nxt_emoji_num][nxt_clipboard_num]:
      dist[nxt_emoji_num][nxt_clipboard_num] = dist[cur_emoji_num][cur_clipboard_num] + 1
      visit[nxt_emoji_num][nxt_clipboard_num] = True
      que.append(nxt)