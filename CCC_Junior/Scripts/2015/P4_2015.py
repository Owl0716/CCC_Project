def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines


friend_dictionary = {}


def build_dictionary(lines):
    clock = 0
    previous_instruction = ''
    for line in lines:
        instruction, friend = line.split()
        if instruction == 'W':
            # print(f"Wait {friend} second!")
            clock += int(friend)
            previous_instruction = instruction
            continue

        if friend_dictionary.get(friend):
            friend_dictionary[friend].append([instruction, clock])
        else:
            friend_dictionary[friend] = []
            friend_dictionary[friend].append([instruction, clock])
        # print(f"clock is: {clock}")

        if not previous_instruction == 'W':
            # print(f"previous instruction = {previous_instruction}")
            clock += 1
        previous_instruction = instruction

def check_each_friend():
    for friend, contacts in friend_dictionary.items():
        total_time = 0
        start = 0
        for contact in contacts:
            instruction, clock = contact
            if instruction == 'R':
                start = clock
            if instruction == 'S':
                duration = clock - start
                # print(f"{friend}: {clock},{duration}")
                total_time += duration
        if len(contacts) % 2 == 1:
            print(f"{friend} -1")
        else:
            print(f"{friend} {total_time}")


def main():
    lines = read_file('../../TextFiles/2015/P4_Input_2015')
    total_lines = lines[0]
    build_dictionary(lines[1:])
    check_each_friend()
    print(friend_dictionary)

if __name__ == '__main__':
    main()
