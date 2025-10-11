def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                n_line = []
                for char in line:
                    if not char == ' ':
                        char = int(char)-1
                        n_line.append(char)


                new_lines.append(n_line)

    return new_lines
future_moves = []
past_moves = []
import copy

def try_move(curr_pos,try_num,board):
    print(try_num)
    print(curr_pos)
    print(board[7][7])
    print(board[curr_pos[1]][curr_pos[0]])
    try:
        if try_num == int(board[curr_pos[1]][curr_pos[0]]):
            try_num += 1
    except:
        asdf = 1

    global past_moves
    future_moves.pop(0)
    if not past_moves == []:
        past_moves.pop(0)
    if past_moves == []:
        past_moves = copy.deepcopy(future_moves)
    for ro in board:
        print(ro)
    moves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
    possible_moves = []
    for move in moves:
        if curr_pos[0]+move[0] > -1 and curr_pos[1]+move[1] <8 and curr_pos[0]+move[0] < 8 and curr_pos[1]+move[1] >-1:
            possible_moves.append([curr_pos[0]+move[0],curr_pos[1]+move[1]])
    for pmove in possible_moves:
        try:
            for m in possible_moves:
                if m not in future_moves:
                    future_moves.append(m)
            if not board[pmove[1]][pmove[0]] == 'S' and not board[pmove[1]][pmove[0]] == 'E':
                if try_num < int(board[pmove[1]][pmove[0]]) or int(board[pmove[1]][pmove[0]]) == 0:
                    board[pmove[1]][pmove[0]] = f'{try_num}'

            elif board[pmove[1]][pmove[0]] == 'E':
                return try_num,0
        except:
            break
    if past_moves ==[]:
        return 0,try_num+1
    else:
        return 0,try_num
def main():
    lines = read_file('../../TextFiles/2010/P5_Input_2010')
    board = []
    for i in range(8):
        row = []
        for f in range(8):
            row.append('0')
        board.append(row)

    starting_pos = lines[0]
    ending_pos = lines[1]

    board[starting_pos[1]][starting_pos[0]] = 'S'
    board[ending_pos[1]][ending_pos[0]] = 'E'
    print(starting_pos)
    current_pos = starting_pos
    try_num = 1
    a = 0
    future_moves.append(current_pos)
    while a == 0:

        a,try_num = try_move(future_moves[0],try_num,board)
    print(a)
if __name__ == '__main__':
    main()