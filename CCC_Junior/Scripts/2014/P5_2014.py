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
    lines = read_file('../../TextFiles/2014/P5_Input_2014')
    num_of_students = int(lines[0])
    students_1 = lines[1].split()
    students_2 = lines[2].split()
    consistent = True
    for i in range(num_of_students):
        if not students_1[i] == ' ' and not students_2[i] ==' ':

            s1 = students_1[i]
            s2 = students_2[i]
            students_1[i] = ' '
            students_2[i] = ' '
            for f in range(num_of_students):
                if s1 == students_2[f]:
                    students_2[f] = ' '
                if s2 == students_1[f]:
                    students_1[f] = ' '
        for g in range(num_of_students):
            if students_1[g] == ' ' and not students_2[g] == ' ' or students_2[g] == ' ' and not students_1[g] == ' ':
                consistent = False
    if consistent:
        print('good')
    else:
        print('bad')


if __name__ == '__main__':
    main()