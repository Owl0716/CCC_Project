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
    lines = read_file('../../TextFiles/2001/P2_Input_2001')
    lines = str(lines)
    y = ''
    k = 0
    f,lines = lines.split('C')
    clubs,lines = lines.split('D')
    diamonds,lines = lines.split('H')
    hearts,spades = lines.split('S')
    y = clubs + diamonds + hearts + spades
    for j in y:
        if j == 'A':
            k+=4
        elif j == 'K':
            k+=3
        elif j == 'Q':
            k+=2
        elif j == 'J':
            k+=1

    if len(clubs) == 0:
        k+=3
    if len(diamonds) == 0:
        k += 3
    if len(hearts) == 0:
        k += 3
    if len(spades) == 0:
        k += 3

    if len(clubs) == 1:
        k+=2
    if len(diamonds) == 1:
        k += 2
    if len(hearts) == 1:
        k += 2
    if len(spades) == 1:
        k += 2

    if len(clubs) == 2:
        k+=1
    if len(diamonds) == 2:
        k += 1
    if len(hearts) == 2:
        k += 1
    if len(spades) == 2:
        k += 1
    print(k)
if __name__ == '__main__':
    main()