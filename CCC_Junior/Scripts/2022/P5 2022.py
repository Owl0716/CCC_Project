def read_file(filepath):
    new_lines = []
    with open(filepath,'r') as file:
        lines = file.readlines()
        for line in lines:
            if not line.strip() == '':
                new_lines.append(line.strip())
    return new_lines
def create_yard(yard_size):
    yard = []
    for i in range(yard_size):
        row = []
        for i in range(yard_size):
            row.append(0)
        yard.append(row)
    return yard
def create_trees(amount_of_trees,tree_coords,yard):
    for i in range(amount_of_trees):
        tree_col, tree_row = tree_coords[i].split(" ")
        col = int(tree_col)
        row = int(tree_row)
        yard[col-1][row-1] = 1
    return yard


def check_possible_tree(row, col, yard,width):
    # print(f"checking width {width}")
    for row_t in range(row,row+width):
        for col_t in range(col, col+width):
            # print(f"{row_t},{col_t} {yard[row_t][col_t]}")
            if yard[row_t][col_t]:
                return False
    return True


def find_max_space(yard, row_x, column):
    yard_size = len(yard)
    for max_width in range(1, yard_size):
        # print(f"range is 1 to {length-max_deepth-1},checking {max_width}")
        if (row_x + max_width) > yard_size or (column + max_width) > yard_size:

            return max_width-1
        if check_possible_tree(row_x, column,yard, max_width):
            # print(f"at least {max_width} for {row_x} and {column}")
            continue
        else:
            # print(f"I hit a tree")
            return max_width-1
    return yard_size

def main():
    # 1. read the question
    lines = read_file("../../TextFiles/2022/P5_Input_2022")
    # 2. create the yard and setup the tree
    yard_size = int(lines[0])
    yard = create_yard(yard_size)
    # print(yard)
    amount_of_trees = int(lines[1])
    yard = create_trees(amount_of_trees,lines[2:],yard)
    # print(yard)
    # print(yard_size)
    # 3. check the max tree space
    # width = find_max_space(yard,0,12)
    # print(f"the width is {width}")
    max_square_length =0
    for row in range(yard_size-1):
        for col in range(yard_size-1):
            if not yard[row][col]:
                width = find_max_space(yard,row,col)
                # print(f"I am checking {row} {col}: with width:{width} ")
                if max_square_length < width:
                    # print(f"I am updating max_square_length to {width}")
                    max_square_length = width
        # print(f"We are on row {row} ")
    print(f"most is  {max_square_length}")
    # for row in yard:
    #     print(row)
    #check_max_space(yard,yard_size)


if __name__ == '__main__':
    main()
