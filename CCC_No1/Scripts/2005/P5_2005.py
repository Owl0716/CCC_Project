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
    lines = read_file('../../TextFiles/2005/P5_Input_2005')
    monkey = None
    for line in lines:
        if line == 'X':
            break


        monkey = True


        for char in range(1,len(line)):
            if line[char] == 'N' and line[char-1] == 'A':
                continue
            elif line[char] == 'A' and line[char-1] == 'N':
                continue
            elif line[char] == 'B' and line[-1] == 'S':
                continue
            else:
                if line[0] == 'B' and line[-1] == 'S':
                    continue
                else:
                    monkey = False
                    break

        if monkey:
            print('Yes')
        elif monkey == False:
            print('NO')

    print(lines)
if __name__ == '__main__':
    main()