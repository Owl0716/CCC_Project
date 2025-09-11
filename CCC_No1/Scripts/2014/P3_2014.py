def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for lines in lines:
            if not lines.strip() == '':
                lines = lines.strip()
                new_lines.append(lines)

    return new_lines

def main():
    lines = read_file('../../TextFiles/2014/P3_Input_2014')
    left = 0
    right = 0
    leftstart = 100
    rightstart = 100
    dice = lines[1:]
    for line in dice:
        left = int(line[0])
        right = int(line[2])
        if left > right:
            rightstart-=left
        elif left < right:
            leftstart-=right
    print(leftstart)
    print(rightstart)



if __name__ == '__main__':
    main()