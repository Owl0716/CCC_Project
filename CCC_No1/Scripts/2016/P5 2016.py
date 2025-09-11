def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines

def make_list(lists,reverse):
    list_cyclists = lists.split(' ')
    if reverse:
        list_cyclists.sort(reverse=True)
    else:
        list_cyclists.sort(reverse=False)
    c = []
    for i in range(len(list_cyclists)):
        if not list_cyclists[i] == ' ':
            c.append(int(list_cyclists[i]))
    return c

def test_name(dmojistan_cyclists,pegland_cyclists,length,question_type):
    lengths = 0
    for i in range(length):
        if question_type == 1:
            if dmojistan_cyclists[i] > pegland_cyclists[i]:
                lengths+= dmojistan_cyclists[i]
                print(dmojistan_cyclists[i])
            else:
                lengths+= pegland_cyclists[i]
                print(pegland_cyclists[i])

        elif question_type == 2:
            if dmojistan_cyclists[i] > pegland_cyclists[i]:
                lengths+= dmojistan_cyclists[i]
                print(dmojistan_cyclists[i])
            else:
                lengths+= pegland_cyclists[i]
                print(pegland_cyclists[i])
    return lengths


def main():
    lines = read_file('../../TextFiles/2016/P5_Input_2016')
    question_type = int(lines[0])
    length = int(lines[1])
    dmojistan_cyclists = []
    pegland_cyclists = []
    if question_type == 1:
        dmojistan_cyclists = make_list(lines[2], True)
        pegland_cyclists = make_list(lines[3], True)
    elif question_type == 2:
        dmojistan_cyclists = make_list(lines[2],False)
        pegland_cyclists = make_list(lines[3],True)
        pegland_cyclists.sort(reverse=True)


    l = test_name(dmojistan_cyclists, pegland_cyclists, length,question_type)


    print(question_type)
    print(pegland_cyclists)
    print(dmojistan_cyclists)
    print(l)

if __name__ == '__main__':
    main()