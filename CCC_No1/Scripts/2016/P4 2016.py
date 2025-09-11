def read_file(file_path):
    with open(file_path, "r") as f:
        line = f.readline()
        line = line.strip()

    return line


def main():
    time = 120
    rush_hour = [7,8,9,15,16,17,18]
    line = read_file('../../TextFiles/2016/P4_Input_2016')
    hour ,minute = line.split(':')
    hour = int(hour)
    minute = float(minute)
    while not time == 0:

        if hour in rush_hour:
            minute+=1
            time -= .5
        else:
            minute+=1
            time -= 1

        if minute >= 60:
            hour+=1
            minute = 0
        if hour >= 24:
            hour = 0
    if len(str(hour)) == 1:
        print(f'0{hour}:{minute}')
    elif len(str(minute)) == 1:
        print(f'{hour}:{minute}0')
    else:
        print(f'{hour}:{minute}')



if __name__ == '__main__':
    main()