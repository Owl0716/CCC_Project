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
    lines = read_file('../../TextFiles/2013/P4_Input_2013')
    total_time = lines[0]
    chorenum = lines[1]
    chores = lines[2:]
    choresdone = 0
    chores.sort()
    for i in range(chorenum):
        if (total_time-chores[i]) >= 0:
            total_time -= chores[i]
            choresdone+=1
        else:
            break
    print(choresdone)
if __name__ == '__main__':
    main()