def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines

def make_list(lists):
    list_cyclists = lists.split(' ')
    c = []
    for i in range(len(list_cyclists)):
        if not list_cyclists[i] == ' ':
            c.append(int(list_cyclists[i]))
    return c

def main():
    lines = read_file('../../TextFiles/2016/P2_Input_2016')
    adds = 0
    f= 0
    for row in lines:
        rs = make_list(row)
        adds+= rs[0]
    for i in range(4):
        a = 0
        for r in range(4):
            ro = make_list(lines[r])
            a+=ro[i]
        if not a == adds:
            print('not magic')
            break
        else:
            f+=1
    if f == 4:
        print('magic')


if __name__ == '__main__':
    main()