def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines


def main():
    touch = ['adgjmptw','behknqux','cfilorv','sz']
    lines = read_file('../../TextFiles/2006/P3_Input_2006')
    line = list(lines[0])
    amount = 0
    previous = ''
    for char in line:
        for i in range(len(touch)):
            if char in touch[i]:
                if previous == '' or not previous == char:
                    previous = char
                    amount+=(i+1)
                else:
                    previous = char
                    amount+=(i+3)
                break
    print(amount)
if __name__ == '__main__':
    main()
