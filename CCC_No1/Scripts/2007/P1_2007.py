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
    lines = read_file('../../TextFiles/2007/P1_Input_2007')
    lines.sort()
    print(lines[1])

if __name__ == '__main__':
    main()