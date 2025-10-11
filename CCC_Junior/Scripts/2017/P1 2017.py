def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(int(line))

    return new_lines

def find_quad(x,y):
    if abs(x) == x and abs(y) == y:
        return 1
    elif not abs(x) == x and abs(y) == y:
        return 2
    elif not abs(x) == x and not abs(y) == y:
        return 3
    else:
        return 4


def main():
    line = read_file('../../TextFiles/2017/P1_Input_2017')

    x = line[0]
    y = line[1]
    quad = find_quad(x,y)
    print(quad)

if __name__ == '__main__':
    main()