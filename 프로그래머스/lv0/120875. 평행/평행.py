def solution(dots):
    delta_list = []
    for i in range(len(dots)):
        for j in range(i+1,len(dots)):
            dx = dots[j][0] - dots[i][0]
            dy = dots[j][1] - dots[i][1]
            print(dx, dy, dy/dx)
            if (dy/dx in delta_list):
                return 1
            delta_list.append(dy/dx)
    return 0