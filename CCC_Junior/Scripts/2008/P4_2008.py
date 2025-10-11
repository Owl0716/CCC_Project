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
    lines = read_file('../../TextFiles/2008/P4_Input_2008')
    question = lines[0].split()
    j = 0
    i=0
    if len(question) > 1:
        while str(question[-1]).isnumeric():
            i+=1
            if i > len(question):
                i = 1
            try:
                int(question[-i])

            except:
                print(question)
                print(-i)
                print(-i+j)
                g = question[-i]
                print(g)
                question.pop(-i)
                question.insert(-i+j,g)
                j+=1
    str_question = ''
    for q in question:
        str_question+=q
        str_question+=' '
    print(str_question)
if __name__ == '__main__':
    main()