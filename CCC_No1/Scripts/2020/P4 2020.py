def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                new_lines.append(line.strip())

    return new_lines


def get_new_string(cyph_list):
    return "".join(cyph_list[1:])+cyph_list[0]

def shift_cyph(cyph):
    new_cyph = []
    for i in range(1, len(cyph)):
        new_cyph.append(cyph[i])
    new_cyph.append(cyph[0])
    return new_cyph


def checkText(cypher, text):
    new_string = cypher
    for i in range(len(cypher)):
        new_string = shift_cyph(new_string)
        new_string = get_new_string(new_string)
        if new_string in text:
            print(f"{new_string}, True, {i+1}")
            return True
    return False

def main():
    #1. read txt file
    lines = read_file('../../TextFiles/2020/P4_Input_2020')
    #2. get variables
    text = lines[0]
    orignal_cypher = lines[1]
    cypher = list(orignal_cypher)
    #3. get result
    check_result, new_string, i = checkText(cypher, text)
    #4. print
    if check_result:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
