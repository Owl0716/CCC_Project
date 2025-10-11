def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(int(line))

    return new_lines
def main():
    lines = read_file('../../TextFiles/2013/P1_Input_2013')
    difference = abs(lines[0]-lines[1])
    oldestchild = lines[1]+difference
    print(oldestchild)


if __name__ == '__main__':
    main()