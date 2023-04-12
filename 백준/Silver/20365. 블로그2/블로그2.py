import sys

N = int(sys.stdin.readline())
colors = sys.stdin.readline().rstrip()
cnt_dict = {'R': 0, 'B': 0}
state = ''
for i in range(len(colors)):
  if state != colors[i]:
    state = colors[i]
    cnt_dict[state] += 1
#print(cnt_dict)
print(min(cnt_dict.values()) + 1)