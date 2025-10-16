def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines
high = ['ace','king','queen','jack']
def find(num,i,lines):
    for j in range(i+1,i+num+1):
        try:
            if lines[j] in high:
                return False
        except:
            return False
    if i%2 == 0:
        c = 'A'
    else:
        c = 'B'
    print(f'Player {c} scores {num} points')
    return True
def main():
    n,m = 0,0
    lines = read_file('../../TextFiles/1999/P1_Input_2019')
    for card in range(len(lines)):
        if not lines[card] in high:
            continue
        if lines[card] == 'ace':
            if find(4,card,lines):
                if card % 2 == 0:
                    n+=4
                else:
                    m+=4
            continue
        elif lines[card] == 'king':
            if find(3,card,lines):
                if card % 2 == 0:
                    n+=3
                else:
                    m+=3
        elif lines[card] == 'queen':
            if find(2,card,lines):
                if card % 2 == 0:
                    n+=2
                else:
                    m+=2
        elif lines[card] == 'jack':
            if find(1,card,lines):
                if card % 2 == 0:
                    n+=1
                else:
                    m+=1
    print(f'Player A: {n}(s).')
    print(f'Player B: {m}(s).')
if __name__ == '__main__':
    main()