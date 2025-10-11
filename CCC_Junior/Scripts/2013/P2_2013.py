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
    lines = read_file('../../TextFiles/2013/P2_Input_2013')
    non_rotatable = ['I','O','S','H','Z','X','N']
    temp = True
    for char in lines[0]:
        if not char in non_rotatable:
            temp = False
            break
    if temp:
        print('YES')
    else:
        print('No')
if __name__ == '__main__':
    main()