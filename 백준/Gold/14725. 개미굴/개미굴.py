import sys

N = int(sys.stdin.readline())
prefix = '--'
pre = []
foods_infos = []
for _ in range(N):
  foods = sys.stdin.readline().split()[1:]
  foods_infos.append(foods)
foods_infos.sort()
same_tree = False
for foods in foods_infos:
  if pre and pre[0] == foods[0]:
    same_tree = True
  for idx, food in enumerate(foods):
    if same_tree and len(pre) > idx:
      if pre[idx] == food:
        continue
      else:
        same_tree = False
        print(prefix * idx + food)
    else:
      print(prefix * idx + food)
  pre = foods
