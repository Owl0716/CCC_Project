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
    lines = read_file('../../TextFiles/2024/P2_Input_2024')
    dusasize = lines[0]
    rest = lines[1:]
    for j in rest:
        if dusasize > j:
            dusasize+=j
        else:
            break
    print(dusasize)
if __name__ == '__main__':
    main()