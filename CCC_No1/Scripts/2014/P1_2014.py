def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(int(line))

    return new_lines
def check_angle_type(lines):
    if lines[0] == lines[1]:
        if lines[1] == lines[2] == 60:
            return 'Equilateral'
        else:
            return 'Isosceles'
    if lines[1] == lines[2]:
        return 'Isosceles'
    else:
        return 'Scalene '
def main():
    lines = read_file('../../TextFiles/2014/P1_Input_2014')
    if lines[0]+ lines[1] + lines[2] == 180:
        type = check_angle_type(lines)
        print(type)
    else:
        print('Error')



if __name__ == '__main__':
    main()