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
    fish_level = read_file('../../TextFiles/2012/P2_Input_2012')
    if fish_level[0] == fish_level[1] == fish_level[2] == fish_level[3]:
        print('Fish At Constant Depth')
    elif fish_level[0] > fish_level[1] > fish_level[2] > fish_level[3]:
        print('Fish Diving')
    elif fish_level[0] < fish_level[1] < fish_level[2] < fish_level[3]:
        print('Fish Rising')
    else:
        print('No Fish')

if __name__ == '__main__':
    main()