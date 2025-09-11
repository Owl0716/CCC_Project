def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines


def decode(amount,message):
    messa = ''
    for i in range(amount):
        a,m = message[i].split(' ')
        mess = ''
        for i in range(int(a)):
            mess += m
        messa = messa + mess +'\n'
    return messa

def main():
    lines = read_file('../../TextFiles/2019/P2_Input_2019')
    amount = int(lines[0])
    rest = lines[1:]
    message = decode(amount,rest)
    print(message)

if __name__ == '__main__':
    main()