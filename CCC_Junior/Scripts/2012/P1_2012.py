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
    lines = read_file('../../TextFiles/2012/P1_Input_2012')
    speed_limit = lines[0]
    speed = lines[1]
    over = 0
    if speed <= speed_limit:
        print('Congratulations, you are within the speed limit!')
    else:
        over = speed-speed_limit
        if over >= 31:
            F = 500
        elif over >= 21:
            F = 270
        else:
            F = 100
        print(f'You are speeding and your fine is ${F}.')
if __name__ == '__main__':
    main()