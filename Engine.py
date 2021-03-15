# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
board = [
    ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
    ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '♗', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    ['♖', '♘', ' ', '♕', '♔', '♗', '♘', '♖']
]
print(board)


# %%
for row in board:
    for piece in row:
        if piece == ' ':
            print('＿', end='   ')
        else:
            print(piece, end='   ')
    print('\n')


# %%
def moves_on_board(x, y):
    if x < 0:
        return False
    elif x > 7:
        return False
    elif y < 0:
        return False
    elif y > 7:
        return False
    else:
        return True
   


# %%


def find_king_moves(x, y):
    for row_offset in range(y - 1, y + 2):
        for col_offset in range(x - 1, x + 2):
            if row_offset != y or col_offset != x:
                if moves_on_board(col_offset, row_offset):
                    print('Considering move to x:', col_offset, 'and y:', row_offset)
    print()


def find_pawn_moves(x, y):
    if y == 6:
        print('Considering move to x:', x, 'and y:', y - 2)
    if moves_on_board(x, y - 1):
        print('Considering move to x:', x, 'and y:', y - 1)
    print()

def find_bishop_moves(x, y):
    for offset in range(1, 8):
        move_x = x - offset
        move_y = y - offset
        if moves_on_board(move_x, move_y):
            print('Considering North-Westward move to x:', move_x, 'and y:', move_y)
    for offset in range(1, 8):
        move_x = x + offset
        move_y = y - offset
        if moves_on_board(move_x, move_y):
            print('Considering North-Eastward move to x:', move_x, 'and y:', move_y)
    for offset in range(1, 8):
        move_x = x + offset
        move_y = y + offset
        if moves_on_board(move_x, move_y):
            print('Considering South-Eastward move to x:', move_x, 'and y:', move_y)
    for offset in range(1, 8):
        move_x = x - offset
        move_y = y + offset
        if moves_on_board(move_x, move_y):
            print('Considering South-Westward move to x:', move_x, 'and y:', move_y)
    print()

    


def find_rook_moves(x, y):
    for xr in range(x + 1, 8):
        print('Considering right move to x:', xr, 'and y:', y)
        target = board[y][xr]
    for xl in range(x - 1, -1, -1):
        print('Considering left move to x:', xl, 'and y:', y)
        target = board[y][xl]
    for yd in range(y + 1, 8):
        print('Considering downward move to x:', x, 'and y:', yd)
        target = board[yd][x]
    for yu in range(y - 1, -1, -1):
        print('Considering upward move to x:', x, 'and y:', yu)
        target = board[yu][x]
    print()

def find_queen_moves(x, y):
    print('♕', 'Found Queen at x:', x, 'and y:', y)
    find_bishop_moves(x, y)
    find_rook_moves(x, y)

def find_all_moves():
    for y in range(len(board)):
        for x in range(len(board[y])):
            piece = board[y][x]
            if piece == '♙':
                print('♙', 'Found Pawn at x:', x, 'and y:', y)
                find_pawn_moves(x, y)
            if piece == '♔':
                print('♔', 'Found King at x:', x, 'and y:', y)
                find_king_moves(x, y)
            if piece == '♖':
                print('♖', 'Found Rook at x:', x, 'and y:', y)
                find_rook_moves(x, y)
            if piece == '♗':
                print('♗', 'Found Bishop at x:', x, 'and y:', y)
                find_bishop_moves(x, y)
            if piece == '♕':
                print('♕', 'Found Queen at x:', x, 'and y:', y)
                find_queen_moves(x, y)

find_all_moves()


# %%



