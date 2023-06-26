from collections import deque


def solution(rc, operations):
    row = deque([deque([r[i] for i in range(1, len(r) - 1)]) for r in rc])
    left_col = deque([r[0] for r in rc])
    right_col = deque([r[-1] for r in rc])
    # print(row)
    # print(left_col)
    # print(right_col)
    def make_board():
        board = []
        for i in range(len(rc)):
            board.append([left_col.popleft()] + list(row.popleft()) + [right_col.popleft()])
        # for i in range(len(board)):
        #     print(board[i])
        return board


    def shift_row():
        row.appendleft(row.pop())
        left_col.appendleft(left_col.pop())
        right_col.appendleft(right_col.pop())

    def rotate():
        row[0].appendleft(left_col.popleft())
        right_col.appendleft(row[0].pop())
        row[-1].append(right_col.pop())
        left_col.append(row[-1].popleft())
    op_dict = {"Rotate": rotate, "ShiftRow": shift_row}
    for operation in operations:
        op_dict[operation]()
    return make_board()