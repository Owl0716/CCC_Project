def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                new_lines.append(line.strip())

    return new_lines


def split_coord(coord):
    x, y = coord.split(",")
    x = int(x)
    y = int(y)
    return x, y


def get_top_left(lines):
    lowest_x = 100
    greatest_y = 0
    top_left = []
    for line in lines:
        x, y = split_coord(line)
        if x < lowest_x and y > greatest_y:
            lowest_x = x
            greatest_y = y
            top_left = x, y
    return top_left


def get_bottom_right(lines):
    greatest_x = 0
    lowest_y = 100
    bottom_right = []
    for line in lines:
        x, y = split_coord(line)
        if x > greatest_x and y < lowest_y:
            greatest_x = x
            lowest_y = y
            bottom_right = x, y
    return bottom_right


def main():
    lines = read_file('../../TextFiles/2020/P3_Input_2020')
    top_left = get_top_left(lines[1:])
    bottom_right = get_bottom_right(lines[1:])

    top_right = bottom_right[0] + 1, top_left[1] + 1
    bottom_left = top_left[0] - 1, bottom_right[1] - 1

    print(bottom_left)
    print(top_right)


if __name__ == '__main__':
    main()
