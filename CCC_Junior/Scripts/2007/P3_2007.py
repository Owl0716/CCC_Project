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
    money = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
    average = 0
    removed = []
    lines = read_file('../../TextFiles/2007/P3_Input_2007')
    offer = lines[-1]
    for i in range(1,lines[0]+1):
        removed.append(money[lines[i]-1])
    for f in removed:
        money.remove(f)
    for amount in money:
        average+=amount
    average/=len(money)
    if offer >= average:
        print('deal')
    else:
        print('no deal')
if __name__ == '__main__':
    main()
