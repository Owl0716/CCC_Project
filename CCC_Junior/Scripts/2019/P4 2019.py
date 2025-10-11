def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines

def flip(times,line,thing):
    for i in range(times):
        if line[i] == 'H':
            p = thing[0]
            thing[0] = thing[1]
            thing[1] = p
        elif line[i] == 'V':
            p = thing[0][0]
            thing[0][0] = thing[0][1]
            thing[0][1] = p


def main():
    thing = [[1,2],[3,4]]
    lines = read_file('../../TextFiles/2019/P4_Input_2019')
    line = lines[0]
    flip(len(line),line,thing)



    for row in thing:
        print(row)

if __name__ == '__main__':
    main()