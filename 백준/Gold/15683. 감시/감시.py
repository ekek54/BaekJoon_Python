import sys
import copy

di2v = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
cam_angle = {1: ['U', 'D', 'L', 'R'], 2: ['UD', 'LR'], 3: ['UR', 'RD', 'DL', 'LU'], 4: ['UDL', 'UDR', 'ULR', 'DLR'],
             5: ['UDLR']}
N, M = map(int, sys.stdin.readline().split())
global office
office = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
cam_info = [(office[i][j], (i, j)) for i in range(N) for j in range(M) if
            1 <= office[i][j] <= 5]  # 사무실에 존재하는 (카메라 모델 번호, 좌표)를 저장한다.
cam_count = len(cam_info)  # 사무실에 존재하는 카메라 개수 저장
ans = []


def dfs(cnt):  # 카메라의 모델을 depth/ 각각의 방향을 width로하는 상태트리 탐색
    global office
    if cnt == cam_count:
        ans.append(sum([office[i].count(0) for i in range(N)]))
        return
    model_num, (x, y) = cam_info[cnt]
    angles = cam_angle[model_num]
    for angle in angles:
        org = copy.deepcopy(office)  # 다음 depth의 dfs가 종료되면 원상태로 되돌아 오기 위해 원보 사무실을 저장한다.
        for di in angle:
            dx, dy = di2v[di]
            tmp_x, tmp_y = x, y
            while 1: #카메라가 볼 수 있는 영역 체크
                nx = tmp_x + dx
                ny = tmp_y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if office[nx][ny] == 0:
                        office[nx][ny] = '#'
                    elif office[nx][ny] == 6:
                        break
                else:
                    break
                tmp_x, tmp_y = nx, ny
        dfs(cnt + 1)
        office = copy.deepcopy(org)


dfs(0)
print(min(ans))
