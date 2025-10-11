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
    lines = read_file('../../TextFiles/2013/P3_Input_2013')
    lines[0] += 1
    while not len(set(list(str(lines[0])))) == len(str(lines[0])):
        lines[0] += 1
    print(lines[0])
if __name__ == '__main__':
    main()