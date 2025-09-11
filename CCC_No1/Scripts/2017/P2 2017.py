def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(int(line))

    return new_lines

def shift(num,org,shiftamount):

    num = num+org*10
    org*=10
    if shiftamount == 1:
        return num
    else:

        return shift(num,org,shiftamount-1)


def main():
    line = read_file('../../TextFiles/2017/P2_Input_2017')

    org = line[0]
    shiftamount = line[1]

    sum = shift(org,org,shiftamount)
    print(sum)

if __name__ == '__main__':
    main()