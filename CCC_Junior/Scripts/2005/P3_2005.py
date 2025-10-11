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

    lines = read_file('../../TextFiles/2005/P3_Input_2005')
    turn_instructions = []
    place = []
    for i in range(0,len(lines),2):
        if lines[i] == 'L':
            turn_instructions.append('RIGHT')
        if lines[i] == 'R':
            turn_instructions.append('LEFT')
    for i in range(1,len(lines),2):
        if i == len(lines)-1:
            continue
        place.append(lines[i])
    place.insert(0,'HOME')
    turn_instructions.reverse()
    place.reverse()

    while not place == ['HOME']:
        print(f'Turn {turn_instructions[0]} onto {place[0]} street.')
        turn_instructions.pop(0)
        place.pop(0)
    print(f'Turn {turn_instructions[0]} into your {place[0]}')
if __name__ == '__main__':
    main()
