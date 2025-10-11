def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readline()
        new_lines.append(int(lines))

    return new_lines
def main():
    lines = read_file('../../TextFiles/2010/P1_Input_2010')
    if not lines[0] % 2 == 0:
        lines[0]-=1
    print(int((lines[0]/2)+1))

if __name__ == '__main__':
    main()