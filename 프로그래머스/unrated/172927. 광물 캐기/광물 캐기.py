def solution(picks, minerals):
  answer = 0
  N = sum(picks)
  key_idx = {"diamond": 0, "iron": 1, "stone": 2}
  energy = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]

  if len(minerals) > N * 5:
    minerals = minerals[: N * 5]
  mineral_groups = [[0, 0, 0] for _ in range(N)]
  for idx, mineral in enumerate(minerals):
    mineral_groups[idx // 5][key_idx[mineral]] += 1
  mineral_groups.sort(key=lambda x: (-x[0], -x[1], -x[2]))
  print(mineral_groups)
  idx = 0
  breaker = False
  for i in range(3):
    for j in range(picks[i]):
      tmp = 0
      for k in range(3):
        tmp += mineral_groups[idx][k] * energy[i][k]
      answer += tmp
      idx += 1
      if idx >= N:
        breaker = True
        break
    if breaker: break
  return answer