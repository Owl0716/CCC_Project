def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for lines in lines:
            if not lines.strip() == '':
                lines = lines.strip()
                new_lines.append(lines)

    return new_lines

def main():
    lines = read_file('../../TextFiles/2014/P2_Input_2014')
    a_num = 0
    b_num = 0
    for char in lines[1]:
        if char == 'A':
            a_num+=1
        else:
            b_num+=1
    if a_num > b_num:
        print('A')
    elif b_num > a_num:
        print('B')
    else:
        print('Tie')





if __name__ == '__main__':
    main()