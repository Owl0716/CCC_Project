def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines

def rotate(rows,rest):
    new_list = []
    for i in range(rows):
        new_row = []
        for s in range(rows):
            # print(f,i)
            new_row.append(rest[s][i])
            # print(new_row)
        new_list.append(new_row)




    newest_list = []
    for f in range(rows):
        newest_row = []
        for i in range(rows):
            newest_row.append(new_list[f][rows-i-1])
        newest_list.append(newest_row)


    return newest_list


def unrotate(rows, rest):
    f = rest
    i=0
    list_of_strings = []
    for i in range(1, rows):
        if not f[i] > f[i - 1] or not f[0][i] > f[0][i - 1]:
            f = rotate(rows,f)
        else:
            break
    if not f[i] > f[i - 1] or not f[0][i] > f[0][i - 1]:
        f = rotate(rows, f)


    for z in range(rows):
        row_of_strings = ''
        for y in range(rows):
            row_of_strings += f' {f[z][y]}'
        list_of_strings.append(row_of_strings)

    return list_of_strings



def main():
    lines = read_file('../../TextFiles/2018/P4_Input_2018')
    rows = int(lines[0])
    old_rest = lines[1:]
    rest = []
    for line in old_rest:
        r = []
        for char in line:
            if not char == ' ':
                r.append(char)
        rest.append(r)
    unrotatedlist = unrotate(rows,rest)
    for row in unrotatedlist:
        print(row)



if __name__ == '__main__':
    main()