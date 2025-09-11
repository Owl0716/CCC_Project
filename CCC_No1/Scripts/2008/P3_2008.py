def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines


def main():
    grid = [['A', 'B', 'C', 'D', 'E', 'F'],
            ['G', 'H', 'I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P', 'Q', 'R'],
            ['S', 'T', 'U', 'V', 'W', 'X'],
            ['Y', 'Z', ' ', '-', '.', 'e']]
    position = [0, 0]
    end = [5,5]
    # for row in grid:
    #     print(row)

    lines = read_file('../../TextFiles/2008/P3_Input_2008')
    word = list(lines[0])
    moves = 0
    for letter in word:
        moves, position = move(grid, letter, moves, position)
    moves, position = move(grid, 'e', moves, position)
    print(moves+1)


def move(grid, letter, moves, position):
    movementsx, position, row = movex(position, letter, grid)
    moves += movementsx
    movementsy, position = movey(position, letter, row)
    moves += movementsy
    return moves, position


def movex(position, letter,grid):
    moves = 0
    diffr = 0
    contain_negative = None
    n_position = position
    rows = []
    for row in range(len(grid)):
        if letter in grid[row]:
            rows.append(grid[row])
            diffr = abs(position[0]-row)
            if '-' in str(position[0]-row):
                contain_negative = True
    moves += diffr

    if contain_negative:
        n_position[0]+=diffr
    else:
        n_position[0]-=diffr

    return moves, n_position,rows
def movey(position, letter,row):
    moves = 0
    diffr = 0
    contain_negative = None
    n_position = position
    for col in range(len(row)):
        if letter in row[col]:
            diffr = abs(position[0]-col)
            if '-' in str(position[0]-col):
                contain_negative = True
    moves += diffr

    if contain_negative:
        n_position[1]-=diffr
    else:
        n_position[1]+=diffr

    return moves, n_position
if __name__ == '__main__':
    main()
