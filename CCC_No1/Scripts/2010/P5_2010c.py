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
                        char = int(char)
                        n_line.append(char)


                new_lines.append(n_line)

    return new_lines

history_moves = []
def make_move(possible_move, end_point, step, path):
    path.append(possible_move)
    new_position_x = possible_move[0]
    new_position_y = possible_move[1]
    if new_position_x == end_point[0] and new_position_y == end_point[1]:
        print(f"I am Done, the path is {path}")
        path.pop()
    elif [new_position_x,new_position_y] in history_moves:
        print(f"I was here before [{new_position_x, new_position_y}]")
        # path.pop()
        return
    else:
        history_moves.append([new_position_x, new_position_y])
        possible_moves = get_possible_moves([new_position_x,new_position_y])
        print(f"from [{new_position_x},{new_position_y}], All possible move are {possible_moves} ")
        for possible_move in possible_moves:
            print(f"the path is {path}")
            make_move(possible_move,end_point,step+1,path)
            path.pop()
        print(f"I have gone through all the moves")


def get_possible_moves(curr_pos):
    moves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
    possible_moves = []
    for move in moves:
        if curr_pos[0] + move[0] > -1 and curr_pos[1] + move[1] < 9 and curr_pos[0] + move[0] < 9 and curr_pos[1] + move[1] > -1:
            possible_moves.append([curr_pos[0] + move[0], curr_pos[1] + move[1]])
    return possible_moves


def main():
    lines = read_file('../../TextFiles/2010/P5_Input_2010')


    starting_pos = lines[0]
    ending_pos = lines[1]
    print(f"start point: {starting_pos}, end point:{ending_pos}")
    current_pos = starting_pos
    possible_moves = get_possible_moves(current_pos)
    path = [starting_pos]
    history_moves.append(starting_pos)
    for possible_move in possible_moves:
        make_move(possible_move,ending_pos,1, path)

if __name__ == '__main__':
    main()