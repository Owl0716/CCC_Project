
def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines

vowels = ["a", "e","i", "o","u"]

def get_ending(line):
    for i in range(1,len(line)):
        if line[-i] in vowels:
            return line[-i:]

def get_rhyme_form(line_endings):
    rhyme_list = ''

    if line_endings[0] == line_endings[1] == line_endings[2] == line_endings[3]:
        rhyme_list += 'perfect, '
    if line_endings[0] == line_endings[1] and line_endings[2] == line_endings[3]:
        rhyme_list += 'even, '
    if line_endings[0] == line_endings[2] and line_endings[1] == line_endings[3]:
        rhyme_list += 'cross, '
    if line_endings[0] == line_endings[3] and line_endings[1] == line_endings[2]:
        rhyme_list += 'shell, '
    if len(rhyme_list) == 0:
        rhyme_list += 'free, '
    return rhyme_list[:-2]


def main():
    poems = []
    lines = read_file('../../TextFiles/2003/poetry.in')
    amount_of_poems = int(lines[0])
    poemss = lines[1:]
    for i in range(amount_of_poems):
        poems.append(poemss[:4])
        for j in range(4):
            poemss.pop(0)
    for k in range(amount_of_poems):
        line_endings = []
        for line in poems[k]:
            f =get_ending(line)
            line_endings.append(f)
        rhymelist = get_rhyme_form(line_endings)
        print(rhymelist)
if __name__ == '__main__':
    main()

