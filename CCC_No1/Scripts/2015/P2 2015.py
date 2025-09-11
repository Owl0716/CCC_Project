def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines
def main():
    lines = read_file('../../TextFiles/2015/P2_Input_2015')
    test = list(lines[0])
    h = 0
    s = 0
    for i in range(len(lines[0])-3):
        if test[i] == ':':
            if test[i+1] == '-':
                if test[i+2] == ')':
                    h+=1
                elif test[i+2] == '(':
                    s+=1
    if h > s:
        print('happy')
    elif h < s:
        print('sad')
    else:
        print('unsure')

if __name__ == '__main__':
    main()