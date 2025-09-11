def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for lines in lines:
            if not lines.strip() == '':
                lines = lines.strip()
                new_lines.append(int(lines))

    return new_lines

def main():
    lines = read_file('../../TextFiles/2014/P4_Input_2014')
    friends = list(range(1,11))
    number_of_friends = lines[0]
    removal_rounds_num = int(lines[1])
    rest = lines[2:]


    for f in range(removal_rounds_num):
        n_friend = []
        for i in range(len(friends)):

            if not (i+1) % int(rest[f]) == 0:
                n_friend.append(friends[i])

            # else:
            #     # print(friends[i])
        friends = n_friend
    string_friends = ''
    for friend in friends:
        string_friends += str(friend)
        string_friends +=' '
    print(string_friends)
if __name__ == '__main__':
    main()