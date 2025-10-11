def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines

def unswap(letter,num,i):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    letter_num = 0
    for g in range(len(alphabet)):
        if alphabet[g] == letter:
            letter_num = g+1
    newletter_num = letter_num-((3*i)+num)
    while newletter_num <=0:

        newletter_num+=26
    # print(letter,((3*i)+num),'TESTS')
    # print()
    return alphabet[newletter_num-1]
    # print()
def main():

    lines = read_file('../../TextFiles/2012/P4_Input_2012')
    s = ''
    for i in range(len(lines[1])):
        f = unswap(f'{lines[1][i]}',int(lines[0]),i+1)
        s+=f
    print(s)
if __name__ == '__main__':
    main()