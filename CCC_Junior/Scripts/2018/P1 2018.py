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
    line = read_file('../../TextFiles/2018/P1_Input_2018')

    one = line[0]
    two = line[1]
    three = line[2]
    four = line[3]
    if one == 9 or 8 and four == 9 or 8 and two == three:
        print('ignore')
    else:
        print('answer')



if __name__ == '__main__':
    main()