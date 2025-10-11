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
    # a = lines[0]
    # b = lines[1]
    # c = lines[2]
    # d = lines[3]
    s = lines[4]
    lines = lines[:4]
    bryon = 0
    nikky = 0

    while s > 1:
        for i in range(len(lines)):

            for f in range(lines[i]):
                if i % 2 == 0:
                    if not i > 1:
                        nikky+=1
                    else:
                        bryon+=1
                else:
                    if not i > 1:
                        nikky-=1
                    else:
                        bryon-=1
                if s <1:
                    break
            s-=(f+1)/2
    if bryon > nikky:
        print('Bryon')
    elif nikky > bryon:
        print('Nikky')
    else:
        print("Tied")

if __name__ == '__main__':
    main()