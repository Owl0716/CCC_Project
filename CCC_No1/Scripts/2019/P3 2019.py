def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines


def decode(lines):
    for line in lines:
        if not line:
            return ""
        result = ''
        count = 1
        for i in range(1, len(line)):
            if line[i] == line[i-1]:
                count += 1
            else:
                result+= (f"{count} {line[i-1]} ")
                count = 1
        result += (f"{count} {line[i-1]} ")
        print(result)

def main():
    lines = read_file('../../TextFiles/2019/P3_Input_2019')
    lines = lines[1:]
    decode(lines)


if __name__ == '__main__':
    main()