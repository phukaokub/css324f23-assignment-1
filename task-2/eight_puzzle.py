import copy


def initial_state():
    return ((7, 2, 4, 5, 0, 6, 8, 3, 1), 1, 1)


def is_goal(s):
    return s[0] == (1, 2, 3, 4, 5, 6, 7, 8, 0)


def successors(s):
    _, r, c = s
    new_r, new_c = r-1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r+1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c-1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c+1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1


def is_valid(r, c):
    return 0 <= r <= 2 and 0 <= c <= 2


def move_blank(s, new_r, new_c):
    board, r, c = s
    new_board = list(board)
    new_board[r*3 + c] = new_board[new_r*3 + new_c]
    new_board[new_r*3 + new_c] = 0
    return (tuple(new_board), new_r, new_c)

def h1(s):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    res = 0
    # The for loop counts the number of elements that is different from
    # the goal configuration.
    # We start from index 1 to 8 because the blank is excluded.
    for idx in range(1, 9):
        if goal[idx] != board[idx]:
            res += 1
    return res

def h3(s):
    board, _, _ = s
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    total_manhattan_distance = 0
    for value in range(1, 9):
        current_row, current_col = find_position(board, value)
        goal_row, goal_col = find_position(goal, value)
        manhattan_distance = abs(current_row - goal_row) + abs(current_col - goal_col)
        total_manhattan_distance += manhattan_distance
    return total_manhattan_distance

def find_position(board, value):
    for row in range(3):
        for col in range(3):
            if board[row * 3 + col] == value:
                return row, col


# def h3(s):
#     # implement this function
#     board, _, _ = s
#     res =0
#     for idx in range(0,8):
#         num = board[idx]
#         r = (num-1)//3
#         c = (num-1)%3
#         r_a = idx//3
#         c_a = idx%3
#         res += math.fabs(r-r_a) + math.fabs(c-c_a)

#     return res