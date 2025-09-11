def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines

#___________Rules
def test(coin_layout):
    print('Nothing just set it to ' ' ')





import copy


def main():

    lines = read_file('../../TextFiles/2012/P5_Input_2012')
    coin_num = int(lines[0])
    coin_layout = list(lines[1])
    coin_layout = make_into_list(coin_layout)
    goal = copy.deepcopy(coin_layout)
    goal.sort()
    print(goal)
    print(coin_layout)


def make_into_list(coin_layout):
    s = []
    for l in coin_layout:

        if not l == ' ':
            s.append(l)
    coin_layout = s
    return coin_layout

if __name__ == '__main__':
    main()