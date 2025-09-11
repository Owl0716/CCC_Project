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
    lines = read_file('../../TextFiles/2011/P2_Input_2011')
    h = lines[0]
    max_hours = lines[1]
    t=1
    a = (-6 * (t ** 4)) + (h * (t ** 3)) + (2 * (t ** 2)) + t
    while a > 0 or t > max_hours:
        t+=1
        a = (-6 * (t ** 4)) + (h * (t ** 3)) + (2 * (t ** 2)) + t
        if t > max_hours:
            break
    if not t > max_hours:
        print('The balloon first touches ground at hour:')
        print(t)
    else:
        print('The balloon does not touch ground in the given time.')
if __name__ == '__main__':
    main()