'''
완탐의 경우
  배열 A의 크기는 최대 1000 x 1000

  배열 B를 만들기 위해서
    B배열 한 칸을 위해 A배열 4칸을 확인한다.
  즉, B생성을 위한 연산은 최대 4 x 1000 x 1000

  배열 B의 값을 구하기 위해서는
    배열 B의 최대 크기는 999 x 999
  1000 x 1000으로 생각할 수 있음

  임의의 행이나 열의 교체에 의한 경우의 수는
    행의 교체의 경우 최대 1000개 중 교체할 2개를 선택 10C2
    열 또한 마찬가지이므로
  총 10C2 x 2 = 90
모든 행 과 열 교체의 경우의 수 별로 B를 생성해서 배열 B의 값을 구한다.
90(경우의 수) x (4 x 1000 x 1000 + 999 x 999)
총 90 x 5,000,000 = 450,000,000 -> 시간 초과

최적화
문제에서 궁금한것은 배열 B가 아닌 배열 B의 값(배열 원소의 총합)
배열 B의 각 원소는 A의 원소가 몇개씩 합쳐져서 만들어 진것
즉, A의 원소들이 각각 몇번 중복되어 B의 원소를 만드는데 사용된지 안다면
한번의 A배열 순회로 B배열의 값을 구할 수 있을 것 같다.
즉, B배의 값을 구하기위한 연산 5,000,000에서 1,000,000 으로 개선 가능
이렇게 개선한다면
90 x 1,000,000 = 90,000,000 -> 시간내 해결 가능

배열 B를 만들기 위해 A의 각 원소가 몇번 더해지는지 직접 for 루프로 확인 결과
[1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
[2, 4, 4, 4, 4, 4, 4, 4, 4, 2]
[2, 4, 4, 4, 4, 4, 4, 4, 4, 2]
[2, 4, 4, 4, 4, 4, 4, 4, 4, 2]
[2, 4, 4, 4, 4, 4, 4, 4, 4, 2]
[2, 4, 4, 4, 4, 4, 4, 4, 4, 2]
[2, 4, 4, 4, 4, 4, 4, 4, 4, 2]
[2, 4, 4, 4, 4, 4, 4, 4, 4, 2]
[2, 4, 4, 4, 4, 4, 4, 4, 4, 2]
[1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
각 꼭지점는 1번 모서리는 2번 그 외는 4번 더해지는 패턴 확인

패턴을 보니 완탐하지 않고 그리디하게 어떤 행 또는 열을 교체할지 판단 가능
모서리에 있는 행/열(122...221)은 그렇지 않은 행/열(244..442)의 반 만큼 더해짐
즉. 모서리에 있는 걸 잘 선택해서 바꿔주면 최대가 된다.

이를 위해
행과 열을 나눠서 생각하고 둘중 결과가 큰 것을 선택한다.
  행의 경우 모든 행의 122...221 배수로한 합을 구한다.
  그 중 모서리중 큰 값을 선택해 모서리가 아닌 것중 가장 작은것과 비교해서
  모서리의 것이 더 크다면 교체하여 배열의 값을 구한다.

  열의 경우는 행과 같다.
'''

import sys


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')


def line_val(line):
  n = len(line)
  result = 0
  for i in range(n):
    if i == 0 or i == n - 1:
      result += line[i]
    else:
      result += line[i] * 2
  return result


def arr_val(line_vals):
  n = len(line_vals)
  result = 0
  for i in range(n):
    if i == 0 or i == n - 1:
      result += line_vals[i]
    else:
      result += (line_vals[i] * 2)
  return result


# 열 또는 행 들의 122...221 배수 합들을 받아서
# greedy하게 최적의 교체를 찾는다.
# 모서리중 큰 값을 선택 모서리가 아닌것 중 가장 작은 값을 선택 둘이 비교해서
# 모서리 값이 더 크면 교체하여
# 배열의 값을 반환하는 함수
def greedy(line_vals: list):
  N = len(line_vals)
  if N == 2:
    return arr_val(line_vals)
  non_edges = line_vals[1: -1]
  min_non_edge_idx = non_edges.index(min(non_edges))
  min_non_edge_idx += 1
  if line_vals[0] > line_vals[-1]:
    max_edge_idx = 0
  else:
    max_edge_idx = N - 1
  if line_vals[min_non_edge_idx] < line_vals[max_edge_idx]:
    line_vals[min_non_edge_idx], line_vals[max_edge_idx] = line_vals[max_edge_idx], line_vals[min_non_edge_idx]
  return arr_val(line_vals)


N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
row_vals = [line_val(A[i]) for i in range(N)]
col_vals = [line_val([A[j][i] for j in range(N)]) for i in range(M)]
row_max = greedy(row_vals)
col_max = greedy(col_vals)
print(max(row_max, col_max))
