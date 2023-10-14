import sys

N, d, k, c = map(int, sys.stdin.readline().split())
c -= 1
sushi_belt = []
for i in range(N):
    sushi_belt.append(int(sys.stdin.readline()) - 1)

my_sushi_dict = {c: 1}

answer = 0

for i in range(k):
    if sushi_belt[i] in my_sushi_dict:
        my_sushi_dict[sushi_belt[i]] += 1
    else:
        my_sushi_dict[sushi_belt[i]] = 1

sushi_kind = len(my_sushi_dict.keys())
answer = sushi_kind


for i in range(N):
    out_sushi = sushi_belt[i]
    in_sushi = sushi_belt[(i + k) % N]
    my_sushi_dict[out_sushi] -= 1
    if my_sushi_dict[out_sushi] == 0:
        del my_sushi_dict[out_sushi]
        sushi_kind -= 1

    if in_sushi in my_sushi_dict:
        my_sushi_dict[in_sushi] += 1
    else:
        my_sushi_dict[in_sushi] = 1
        sushi_kind += 1
    answer = max(answer, sushi_kind)

print(answer)