def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines

def add_every(rest):
    new_rest = []
    for f in range(len(rest)):
        for i in range(len(rest[f])):
            if not rest[0][i] == ' ' and not i == 0:
                new_rest.append(int(rest[f][i]))
    return new_rest
def check_end(rest):
    ends = []
    for f in range(len(rest)):
        if int(rest[f][0]) == 0:
            ends.append(f+1)
    return ends
def every_page_readable(pages,rest):
    new_rest = add_every(rest)
    for i in range(2,pages+1):

        if not i in new_rest:

            return False
    return True

def make_into_list(rest):
    list_of_rest =[]
    for f in range(len(rest)):
        list_of_row = []
        for i in range(len(rest[f])):
            if not rest[f][i] == ' ':
                list_of_row.append(rest[f][i])
        list_of_rest.append(list_of_row)
    return list_of_rest

def shortpath(current_option,rest,steps,end):
    print(current_option)
    if current_option[-1] == 0 or current_option[-1] > steps:
        current_option[-1] = steps
    if int(current_option[0]) == 0:
        return steps
    else:
        for i in range(1, len(current_option)-1):

            for f in end:
                if str(f) in current_option:
                    return shortpath(rest[f-1],rest, steps,end)

        return shortpath(rest[int(current_option[-3])],rest, steps+1,end)

def shortest_path(rest,steps):
    new_rest = make_into_list(rest)
    end = check_end(rest)
    for i in range(len(new_rest)):
        new_rest[i].append(0)
    shortestpath= shortpath(new_rest[0] , new_rest , steps,end)
    return shortestpath

def main():
    lines = read_file('../../TextFiles/2018/P5_Input_2018')
    pages = int(lines[0])
    rest = lines[1:]
    steps = 1
    every_page_reachable = every_page_readable(pages,rest)
    shortestpath = shortest_path(rest,steps)
    print(every_page_reachable)
    print(shortestpath+1)

if __name__ == '__main__':
    main()