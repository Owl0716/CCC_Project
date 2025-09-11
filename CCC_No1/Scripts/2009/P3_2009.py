def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(int(line))

    return new_lines

def time_adjust(hour,minute,adjust_value):

    if '-' in str(adjust_value):
        for i in range(abs(adjust_value)):
            minute-=1
            if minute <= 0:
                minute = 59
                hour-=1
            if hour ==0:
                hour = 23
                minute = 59
        minute+=(adjust_value/-60)
        minute = int(minute)
        if minute > 59:
            minute = 0
            hour += 1
        if hour >= 24:

            hour = 0

    else:
        for i in range(abs(adjust_value)):

            minute+=1

            if minute > 59:

                minute= 0
                hour+=1
            if hour >= 24:

                hour=0
    if len(str(minute)) < 2:
        return f"{hour}{minute}0 in"
    else:
        return f"{hour}{minute} in"



def main():
    lines = read_file('../../TextFiles/2009/P3_Input_2009')
    s = str(lines[0])
    hour = int(s[:2])
    minute = int(s[2:])
    dif = [0,-180,-120,-60,0,60,90]
    for i in range(7):
        start = time_adjust(hour,minute,dif[i])
        if i == 0:
            s ='Ottawa'
        if i == 1:
            s = 'Victoria'
        if i == 2:
            s = 'Edmonton'
        if i == 3:
            s = 'Winnipeg'
        if i == 4:
            s = 'Toronto'
        if i == 5:
            s = 'Halifax'
        if i == 6:
            s = 'St. John’s'
        print(start,s)






if __name__ == '__main__':
    main()