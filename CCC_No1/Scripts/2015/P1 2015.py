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
    lines = read_file('../../TextFiles/2015/P1_Input_2015')
    month = int(lines[0])
    day = int(lines[1])
    if month > 2:
        print('After')
    elif month < 2:
        print('Before')
    else:
        if day > 18:
            print('After')
        elif day < 18:
            print('Before')
        else:
            print('Special')


if __name__ == '__main__':
    main()