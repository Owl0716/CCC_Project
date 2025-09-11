def read_file(file_path):
    new_lines = []
    with open(file_path,"r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                new_lines.append(line.strip())

    return new_lines

def check_direction(line, direction):
    sum = int(line[0]) + int(line[1])
    if sum == 0:
        return f"{direction} {line[2:]}", direction
    elif sum % 2 == 0:
        return f"right {line[2:]}", "right"
    else:
        return f"left {line[2:]}", "left"


def main():
    lines = read_file("../../TextFiles/2021/P3_Input_2021")
    same = ""
    for line in lines:
        if line != '99999':
            instruction, same = check_direction(line, same)
            print(instruction)
        else:
            break


if __name__ == '__main__':
    main()