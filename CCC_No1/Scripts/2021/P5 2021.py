def read_file(file_path):
    new_lines = []
    with open(file_path,"r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                new_lines.append(line.strip())

    return new_lines
#Nuthing wrong here
def make_board(col_size,row_size):
    board = []
    for i in range(col_size):
        row = []
        for i in range(row_size):
            row.append("B")
        board.append(row)
    return board
#100% FLIPPING CORRECT
def turn_gold(type,num,board,row,col):
    if type == 'R':
        for i in range(col):
            if board[num][i-1] == 'B':
                board[num][i-1] = 'G'
            elif board[num][i-1] == 'G':
                board[num][i-1] = 'B'
    elif type == 'C':
        for i in range(row):
            if board[i-1][num] == 'B':
                board[i-1][num] = 'G'
            elif board[i-1][num] == 'G':
                board[i-1][num] = 'B'


def main():
    lines = read_file("../../TextFiles/2021/P5_Input_2021")
    col_size = int(lines[1])
    row_size = int(lines[0])
    command_num = int(lines[2])
    board = make_board(row_size,col_size)
    print(col_size, row_size)
    for i in range(3,command_num+3):

        type,num = lines[i].split(" ")
        # print(type, num)

        turn_gold(type,int(num)-1,board,row_size,col_size)


    for row in board:
        print(row)



if __name__ == '__main__':
    main()