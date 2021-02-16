import sys
sudoku= list()
for i in range(9):
    line=list(list(map(int,sys.stdin.readline().split(' '))))
    sudoku.append(line)
#빈칸 개수 구하기
N = 0
blanks=list()
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            blanks.append((i,j))
            N +=1
def promising(cnt,x):
    #가로확인
    for i in range(9):
        if sudoku[blanks[cnt][0]][i]==x:
            return 0
    #세로 확인
    for i in range(9):
        if sudoku[i][blanks[cnt][1]]== x:
            return 0
    # 속하는 3x3정사각형 위치 찾기
    a = blanks[cnt][0] // 3
    b = blanks[cnt][1] // 3
    #3x3 정사각형 확인
    for i in range(3):
        for j in range(3):
            if sudoku[3*a+i][3*b+j] == x:
                return 0
    return 1

def dfs(cnt):
    if (cnt == N):
        for i in sudoku:
            for j in i:
                print(j,end=' ')
            print('')
        exit()
    for j in range(1,10):
        if promising(cnt,j) == 0:
            continue
        sudoku[blanks[cnt][0]][blanks[cnt][1]] = j
        dfs(cnt + 1)
        sudoku[blanks[cnt][0]][blanks[cnt][1]] = 0
dfs(0)
