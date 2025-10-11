def read_file(file_path):
    new_lines = []
    new_char = []
    with open(file_path,"r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                new_lines.append(line.strip())
        for char in new_lines[0]:
            if char == 'L':
                new_char.append(3)
            if char == 'M':
                new_char.append(2)
            if char == 'S':
                new_char.append(1)

    return new_char
def check_books(book_one, book_two):
    if not book_one >= book_two:
        return True
    else:
        return False
def main():
    switches = 0
    lines =read_file("../../TextFiles/2021/P4_Input_2021")
    for i in range(len(lines)-1):
        for i in range(len(lines)-1):
            change = check_books(lines[i], lines[i + 1])
            if change:
                temp = lines[i]
                lines[i] = lines[i+1]
                lines[i+1] = temp
                switches+=1
    for i in range(len(lines)):
        if lines[i] == 3:
            lines[i] = 'L'
        elif lines[i] == 2:
            lines[i] = 'M'
        else:
            lines[i] = 'S'
    print(lines)
    print(switches)
if __name__ == '__main__':
    main()