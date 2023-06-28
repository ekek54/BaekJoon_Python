import sys

global cube
cube = {'U': [['w' for j in range(3)] for i in range(3)],
        'D': [['y' for j in range(3)] for i in range(3)],
        'F': [['r' for j in range(3)] for i in range(3)],
        'B': [['o' for j in range(3)] for i in range(3)],
        'L': [['g' for j in range(3)] for i in range(3)],
        'R': [['b' for j in range(3)] for i in range(3)],
        }


def rotate(matrix, r):
    if r == '+':
        return [[matrix[2 - j][i] for j in range(3)] for i in range(3)]
    if r == '-':
        return [[matrix[j][2 - i] for j in range(3)] for i in range(3)]


def side_effect(UDFBLR, r):
    if UDFBLR == 'U':
        if r == '+':
            cube['F'][0], cube['L'][0], cube['B'][0], cube['R'][0] = cube['R'][0], cube['F'][0], cube['L'][0], \
                                                                     cube['B'][0]
        else:
            cube['F'][0], cube['L'][0], cube['B'][0], cube['R'][0] = cube['L'][0], cube['B'][0], cube['R'][0], \
                                                                     cube['F'][0]
    elif UDFBLR == 'D':
        if r == '+':
            cube['F'][2], cube['L'][2], cube['B'][2], cube['R'][2] = cube['L'][2], cube['B'][2], cube['R'][2], \
                                                                     cube['F'][2]
        else:
            cube['F'][2], cube['L'][2], cube['B'][2], cube['R'][2] = cube['R'][2], cube['F'][2], cube['L'][2], \
                                                                     cube['B'][2]
    elif UDFBLR == 'F':
        if r == "+":
            tmp = ['' for _ in range(3)]
            for i in range(3):
                tmp[i] = cube['U'][2][i]
            for i in range(3):
                cube['U'][2][i] = cube['L'][2 - i][2]
            for i in range(3):
                cube['L'][i][2] = cube['D'][0][i]
            for i in range(3):
                cube['D'][0][i] = cube['R'][2 - i][0]
            for i in range(3):
                cube['R'][i][0] = tmp[i]
        else:
            tmp = ['' for _ in range(3)]
            for i in range(3):
                tmp[i] = cube['U'][2][i]
            for i in range(3):
                cube['U'][2][i] = cube['R'][i][0]
            for i in range(3):
                cube['R'][i][0] = cube['D'][0][2 - i]
            for i in range(3):
                cube['D'][0][i] = cube['L'][i][2]
            for i in range(3):
                cube['L'][i][2] = tmp[2 - i]

    elif UDFBLR == 'L':
        if r == "+":
            tmp = ['' for _ in range(3)]
            for i in range(3):
                tmp[i] = cube['U'][i][0]
            for i in range(3):
                cube['U'][i][0] = cube['B'][2 - i][2]
            for i in range(3):
                cube['B'][i][2] = cube['D'][2 - i][0]
            for i in range(3):
                cube['D'][i][0] = cube['F'][i][0]
            for i in range(3):
                cube['F'][i][0] = tmp[i]
        else:
            tmp = ['' for _ in range(3)]
            for i in range(3):
                tmp[i] = cube['U'][i][0]
            for i in range(3):
                cube['U'][i][0] = cube['F'][i][0]
            for i in range(3):
                cube['F'][i][0] = cube['D'][i][0]
            for i in range(3):
                cube['D'][i][0] = cube['B'][2 - i][2]
            for i in range(3):
                cube['B'][i][2] = tmp[2 - i]
    elif UDFBLR == 'B':
        if r == "+":  # uldr -> ruld
            tmp = ['' for _ in range(3)]
            for i in range(3):
                tmp[i] = cube['U'][0][i]
            for i in range(3):
                cube['U'][0][i] = cube['R'][i][2]
            for i in range(3):
                cube['R'][i][2] = cube['D'][2][2 - i]
            for i in range(3):
                cube['D'][2][i] = cube['L'][i][0]
            for i in range(3):
                cube['L'][i][0] = tmp[2 - i]
        else:
            tmp = ['' for _ in range(3)]
            for i in range(3): #uldr -> ldru
                tmp[i] = cube['U'][0][i]
            for i in range(3):
                cube['U'][0][i] = cube['L'][2 - i][0]
            for i in range(3):
                cube['L'][i][0] = cube['D'][2][i]
            for i in range(3):
                cube['D'][2][i] = cube['R'][2 - i][2]
            for i in range(3):
                cube['R'][i][2] = tmp[i]
    else:
        if r == "+": #ufdb -> fdbu
            tmp = ['' for _ in range(3)]
            for i in range(3):
                tmp[i] = cube['U'][i][2]
            for i in range(3):
                cube['U'][i][2] = cube['F'][i][2]
            for i in range(3):
                cube['F'][i][2] = cube['D'][i][2]
            for i in range(3):
                cube['D'][i][2] = cube['B'][2 - i][0]
            for i in range(3):
                cube['B'][i][0] = tmp[2 - i]
        else:#ufdb-> bufd
            tmp = ['' for _ in range(3)]
            for i in range(3):
                tmp[i] = cube['U'][i][2]
            for i in range(3):
                cube['U'][i][2] = cube['B'][2 - i][0]
            for i in range(3):
                cube['B'][i][0] = cube['D'][2 - i][2]
            for i in range(3):
                cube['D'][i][2] = cube['F'][i][2]
            for i in range(3):
                cube['F'][i][2] = tmp[i]

def init_cube():
    global cube
    cube = {'U': [['w' for j in range(3)] for i in range(3)],
        'D': [['y' for j in range(3)] for i in range(3)],
        'F': [['r' for j in range(3)] for i in range(3)],
        'B': [['o' for j in range(3)] for i in range(3)],
        'L': [['g' for j in range(3)] for i in range(3)],
        'R': [['b' for j in range(3)] for i in range(3)],
        }

def pb(matrix):
    for i in range(len(matrix)):
        print("".join(matrix[i]))


T = int(sys.stdin.readline())
for _ in range(T):
    init_cube()
    N = int(sys.stdin.readline())
    operations = list(sys.stdin.readline().split())
    for i, operation in enumerate(operations):
        UDFBLR, r = list(operation)
        cube[UDFBLR] = rotate(cube[UDFBLR], r)
        side_effect(UDFBLR, r)
        # print(cube)
    pb(cube['U'])
