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
    lines = read_file('../../TextFiles/2004/P3_Input_2004')
    adjective_num = int(lines[0])
    noun_num = int(lines[1])
    r = lines[2:]
    adjective_list  = r[:adjective_num]
    noun_list = r[adjective_num:]
    for adjective in adjective_list:
        for noun in noun_list:
            print(adjective,'as',noun)

if __name__ == '__main__':
    main()
