def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines
def find_same_parking(parking_spots,yesturday,today):
    a = 0
    for i in range(parking_spots):
        if yesturday[i] == today[i] == 'C':
            a+=1
    return a


def main():
    line = read_file('../../TextFiles/2018/P2_Input_2018')
    parking_spots = int(line[0])
    yesturday = line[1]
    today = line[2]

    amount =find_same_parking(parking_spots,yesturday,today)
    print(amount)


if __name__ == '__main__':
    main()