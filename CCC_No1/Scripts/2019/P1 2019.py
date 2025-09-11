def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(int(line))

    return new_lines
def winner(three,two,one):
    if three[0]+two[0]+one[0]>three[1]+two[1]+one[1]:
        return 1
    elif three[0]+two[0]+one[0]<three[1]+two[1]+one[1]:
        return 2
    else:
        return 3

def main():
    lines = read_file('../../TextFiles/2019/P1_Input_2019')
    three_pointers = lines[0]*3, lines[3]*3
    two_pointers = lines[1]*2, lines[4]*2
    one_pointers = lines[2], lines[5]
    apples = winner(three_pointers,two_pointers,one_pointers)
    if apples == 1:
        print('A')
    elif apples == 2:
        print('B')
    else:
        print('T')


if __name__ == '__main__':
    main()
