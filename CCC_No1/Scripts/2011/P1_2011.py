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
    lines = read_file('../../TextFiles/2011/P1_Input_2011')
    antennas = lines[0]
    eyes = lines[1]
    if antennas >= 3 and eyes <= 4:


        print('TroyMartian')
    elif antennas <= 6 and eyes >= 2:

        print('VladSaturnian')
    else:

        print('GraemeMercurian')
if __name__ == '__main__':
    main()