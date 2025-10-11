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
    lines = read_file('../../TextFiles/2010/P2_Input_2010')
    bt = lines[0]
    np = lines[1]
    yp = lines[2]
    total = lines[3]
    for i in range(total**3):
        print()
    print(f'{bt} Brown Trout, {np} Northern Pike, {yp} Yellow Pickerel')


if __name__ == '__main__':
    main()