# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
board = [
    [' ', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
    ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '♜', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
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
def colour_of_piece(piece):
    if piece == '♙':
        return 'white'
    elif piece == '♖':
        return 'white'
    elif piece == '♘':
        return 'white'
    elif piece == '♗':
        return 'white'
    elif piece == '♕':
        return 'white'
    elif piece == '♔':
        return 'white'
    elif piece == ' ':
        return 'empty'
    else:
        return 'black'


# %%
def direction_move(direction):
    if direction == 'north':
        return 0, -1
    if direction == 'north-east':
        return 1, -1
    if direction == 'east':
        return 1, 0
    if direction == 'south-east':
        return 1, 1
    if direction == 'south':
        return 0, 1
    if direction == 'south-west':
        return -1, 1
    if direction == 'west':
        return -1, 0
    if direction == 'north-west':
        return -1, -1
    


# %%
def find_moves_in_direction(x_pos, y_pos, our_colour, direction, max_moves):
    x_off, y_off = direction_move(direction)
    x_target = x_pos
    y_target = y_pos
    for moves in range(max_moves):
        x_target += x_off
        y_target += y_off
        if not moves_on_board(x_target, y_target):
            break
        target = board[y_target][x_target]
        target_colour = colour_of_piece(target)
        if our_colour == target_colour:
            print('Blocked by', target+'. Now ending search in', direction+ 'ward direction')
            break
        print('Considering North-Westward move to x:', x_target, 'and y:', y_target)
        if our_colour != target_colour and target_colour != 'empty': 
            print('Taking', target+'. Now ending search in', direction+'ward direction')
            break


# %%
def find_king_moves(x, y):
    # TODO use find moves in direction function to check for blocking and capture
    for row_offset in range(y - 1, y + 2):
        for col_offset in range(x - 1, x + 2):
            if row_offset != y or col_offset != x:
                if moves_on_board(col_offset, row_offset):
                    print('Considering move to x:', col_offset, 'and y:', row_offset)
                
    print()


def find_pawn_moves(x, y, our_colour):
    if our_colour == 'white':
        if y == 6:
            find_moves_in_direction(x, y, our_colour, 'north', 2)
        else:
            find_moves_in_direction(x, y, our_colour, 'north', 1)
    if our_colour == 'black':
        if y == 1:
            find_moves_in_direction(x, y, our_colour, 'south', 2)
        else:
            find_moves_in_direction(x, y, our_colour, 'south', 1)    
    print()

def find_bishop_moves(x, y, our_colour):
    for i in ['north-east', 'south-east', 'south-west', 'north-west']:
        find_moves_in_direction(x, y, our_colour, i, 8)
    print()

def find_rook_moves(x, y, our_colour):
    for i in ['north','east', 'south', 'west']:
        find_moves_in_direction(x, y, our_colour, i, 8)
    print()

def find_queen_moves(x, y, our_colour):
    print('♕', 'Found Queen at x:', x, 'and y:', y)
    find_bishop_moves(x, y, our_colour)
    find_rook_moves(x, y, our_colour)
    print()

def find_horsie_moves(x, y):
    # TODO intergrate into direction moves function and add blocking and capture
    if moves_on_board(x - 1, y - 2):
        print('Considering two Up and one Left at x:', x - 1, 'and y:', y - 2)
    if moves_on_board(x + 1, y - 2):
        print('Considering two Up and one Right at x:', x + 1, 'and y:', y - 2)
    if moves_on_board(x + 2, y - 1):
        print('Considering one Up and two Right at x:', x + 2, 'and y:', y - 1)
    if moves_on_board(x + 2, y + 1):
        print('Considering one Down and two Right at x:', x + 2, 'and y:', y + 1)
    if moves_on_board(x + 1, y + 2):
        print('Considering two Down and one Right at x:', x + 1, 'and y:', y + 2)
    if moves_on_board(x - 1, y + 2):
        print('Considering two Down and one Left at x:', x - 1, 'and y:', y + 2)
    if moves_on_board(x - 2, y + 1):
        print('Considering one Down and two Left at x:', x - 2, 'and y:', y + 1)
    if moves_on_board(x - 2, y - 1):
        print('Considering one Up and two Left at x:', x - 2, 'and y:', y - 1)
    print()


# %%
def find_all_moves(move_colour):
    # TODO check all moves is valid
    # TODO store moves
    for y in range(len(board)):
        for x in range(len(board[y])):
            piece = board[y][x]
            colour = colour_of_piece(piece)
            if move_colour == colour:
                if piece == '♙' or piece == '♟':
                    print(piece, 'Found Pawn at x:', x, 'and y:', y)
                    find_pawn_moves(x, y, move_colour)
                if piece == '♔' or piece == '♚':
                    print(piece, 'Found King at x:', x, 'and y:', y)
                    find_king_moves(x, y)
                if piece == '♖' or piece == '♜':
                    print(piece, 'Found Rook at x:', x, 'and y:', y)
                    find_rook_moves(x, y, move_colour)
                if piece == '♗' or piece == '♝':
                    print(piece, 'Found Bishop at x:', x, 'and y:', y)
                    find_bishop_moves(x, y, move_colour)
                if piece == '♕' or piece == '♛':
                    print(piece, 'Found Queen at x:', x, 'and y:', y)
                    find_queen_moves(x, y, move_colour)
                if piece == '♘' or piece == '♞':
                    print(piece, 'Found Horsie at x:', x, 'and y:', y)
                    find_horsie_moves(x, y)

find_all_moves('black')


# %%
#print(target_colour) 
#print(our_colour)
#print(target)


