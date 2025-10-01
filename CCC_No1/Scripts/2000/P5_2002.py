def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines

dic = {}
paths = []
def main():
    global dic
    lines = read_file('../../TextFiles/2001/P5_Input_2001')
    lines = lines[:-1]
    camps = create_camps(dic, lines)
    add_roads(dic, lines)
    check_paths('A',len(lines))
    for j in range(10):
        for k in camps:

            for j in paths:
                if not k in j:
                    i = camps.index(k)
                    camps.pop(i)

                    break
    bestbomb = []
    for g in camps:
        for k in camps:
            if not g == k:
                if k in dic[g]:
                    road = ''
                    road = g+k
                    if road in lines:
                        print(road)
def add_roads(dic, lines):
    for q in lines:
        for r in range(len(q)):
            if r == 1:
                dic[q[r]].append(q[0])
            else:
                dic[q[r]].append(q[1])
def create_camps(dic, lines):
    camps = []
    for j in lines:
        for k in j:
            camps.append(k)
    camps = sorted(list(set(camps)))
    for camp in camps:
        dic[camp] = []
    return camps[2:]
def check_paths(current_path,count):
    current_camp = current_path[-1]

    current_options = dic[current_camp]
    for j in current_options:
        check_path(current_path,count)
def check_path(current_path,count):
    if count == 0:
        return
    current_camp = current_path[-1]
    if current_camp == 'B':
        paths.append(current_path)
        return
    current_options = dic[current_camp]
    for j in current_options:
        try:
            if not j in current_path:
                check_path(current_path+j,count-1)
        except:
            return
if __name__ == '__main__':
    main()