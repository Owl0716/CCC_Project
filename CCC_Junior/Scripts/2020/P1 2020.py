def read_file(file_path):
    new_lines = []
    with open(file_path,"r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                new_lines.append(line.strip())

    return new_lines
def happiness(S,M,L):
    happylevel = 0
    happylevel += 1*S
    happylevel +=2*M
    happylevel += 3*L
    if happylevel >= 10:
        return True
    else:
        return False

def main():
    lines = read_file('../../TextFiles/2020/P1_Input_2020')
    happy = happiness(int(lines[0]),int(lines[1]), int(lines[2]))
    if happy:
        print("happy")
    else:
        print("sad")

if __name__ == '__main__':
    main()