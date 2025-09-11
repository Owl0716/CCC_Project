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
    lines = read_file('../../TextFiles/2016/P1_Input_2016')
    test = 0
    for i in range(len(lines)):
        if lines[i] == 'W':
            test+=1
    if test == 5 or test == 6:
        print(1)
    elif test == 3 or test == 4:
        print(2)
    elif test == 1 or test == 2:
        print(3)
    else:
        print(-1)


if __name__ == '__main__':
    main()