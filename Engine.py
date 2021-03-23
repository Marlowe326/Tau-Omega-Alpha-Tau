# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import random
import time
from IPython.display import clear_output


# %%
board = [
    ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
    ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
]
print(board)


# %%
def print_board():
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
    piece_moves = []
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
            #print('Blocked by', target +'. Now ending search in', direction + 'ward direction')
            break
        #print('Considering', direction + 'ward move to x:', x_target, 'and y:', y_target)
        piece_moves.append(((x_pos, y_pos), (x_target, y_target)))
        if our_colour != target_colour and target_colour != 'empty': 
           #print('Taking', target+'. Now ending search in', direction +'ward direction')
            break
    return piece_moves


# %%
def find_king_moves(x, y, our_colour):
    king_moves = []
    for i in ['north', 'north-east', 'east', 'south-east', 'south', 'south-west', 'west', 'north-west']:
        king_moves.extend(find_moves_in_direction(x, y, our_colour, i, 1))
    #print()
    return king_moves

def find_pawn_moves(x, y, our_colour):
    # TODO fix pawn moves captrure bug
    pawn_moves = []
    if our_colour == 'white':
        if y == 6:
            pawn_moves.extend(find_moves_in_direction(x, y, our_colour, 'north', 2))
        else:
            pawn_moves.extend(find_moves_in_direction(x, y, our_colour, 'north', 1))
    if our_colour == 'black':
        if y == 1:
            pawn_moves.extend(find_moves_in_direction(x, y, our_colour, 'south', 2))
        else:
            pawn_moves.extend(find_moves_in_direction(x, y, our_colour, 'south', 1))    
    #print()
    return pawn_moves

def find_bishop_moves(x, y, our_colour):
    bishop_moves = []
    for i in ['north-east', 'south-east', 'south-west', 'north-west']:
        bishop_moves.extend(find_moves_in_direction(x, y, our_colour, i, 8))
    #print()
    return bishop_moves

def find_rook_moves(x, y, our_colour):
    rook_moves = []
    for i in ['north','east', 'south', 'west']:
        rook_moves.extend(find_moves_in_direction(x, y, our_colour, i, 8))
    #print()
    return rook_moves

def find_queen_moves(x, y, our_colour):
    queen_moves = []
    queen_moves.extend(find_bishop_moves(x, y, our_colour))
    queen_moves.extend(find_rook_moves(x, y, our_colour))
    #print()
    return queen_moves

def find_horsie_moves(x, y, our_colour):
    horsie_moves = []
    for horiz_offset, vertic_offset in [ (2, 1), (1, 2), (-2, 1), (1, -2) ]:
        for direction in [1, -1]:
            x_offset = horiz_offset * direction
            y_offset = vertic_offset * direction
            x_target = x + x_offset
            y_target = y + y_offset
            if not moves_on_board(x_target, y_target):
                continue
            target = board[y_target][x_target]
            target_colour = colour_of_piece(target)
            if our_colour == target_colour:
                #print('Blocked by', target + '. Now ending search in a direction')
                continue
            #print('Considering a move to x:', x_target, 'and y:', y_target)
            horsie_moves.append(((x, y), (x_target, y_target)))
            if our_colour != target_colour and target_colour != 'empty': 
                #print('Taking', target+'. Now ending search in a direction')
                continue
    #print()
    return horsie_moves


# %%
def find_all_moves(move_colour):
    all_moves = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            piece = board[y][x]
            colour = colour_of_piece(piece)
            if move_colour == colour:
                if piece == '♙' or piece == '♟':
                    #print(piece, 'Found Pawn at x:', x, 'and y:', y)
                    all_moves.extend(find_pawn_moves(x, y, move_colour))
                if piece == '♔' or piece == '♚':
                    #print(piece, 'Found King at x:', x, 'and y:', y)
                    all_moves.extend(find_king_moves(x, y, move_colour))
                if piece == '♖' or piece == '♜':
                    #print(piece, 'Found Rook at x:', x, 'and y:', y)
                    all_moves.extend(find_rook_moves(x, y, move_colour))
                if piece == '♗' or piece == '♝':
                    #print(piece, 'Found Bishop at x:', x, 'and y:', y)
                    all_moves.extend(find_bishop_moves(x, y, move_colour))
                if piece == '♕' or piece == '♛':
                    #print(piece, 'Found Queen at x:', x, 'and y:', y)
                    all_moves.extend(find_queen_moves(x, y, move_colour))
                if piece == '♘' or piece == '♞':
                   #print(piece, 'Found Horsie at x:', x, 'and y:', y)
                    all_moves.extend(find_horsie_moves(x, y, move_colour))
    return all_moves

find_all_moves('black')


# %%
def choose_moves(list_of_moves):
    # TODO value pieces
    return (random.choice(list_of_moves))


# %%
def make_move(move):
    from_pos, to_pos = move
    from_x, from_y = from_pos
    to_x, to_y = to_pos

    moving_piece = board[from_y][from_x]
    board[to_y][to_x] = moving_piece
    board[from_y][from_x]= ' '


# %%
colour = 'white'
while True:
    clear_output(wait=True)
    print_board()
    move_list = find_all_moves(colour)
    chosen_move = choose_moves(move_list)
    make_move(chosen_move)
    if colour == 'white':
        colour = 'black'
    else: 
        colour = 'white'
    time.sleep(2.5) 
    print()
    print()


# %%



