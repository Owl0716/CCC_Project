def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines

dic ={}

def main():
    lines = read_file('../../TextFiles/2011/P4_Input_2011')

if __name__ == '__main__':
    main()