def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines
def convert(s):
    sx,sy = s.split(' ')
    sx = int(sx)
    sy = int(sy)
    return sx,sy

def ispossible(start,destination,units):
    startx,starty = convert(start)
    destinationx, destinationy = convert(destination)

    differencex = abs(startx-destinationx)
    differencey = abs(starty-destinationy)
    difference = differencex+differencey
    if difference > units:
        return False
    if difference % 2 == 0 and units % 2 == 0 or not difference % 2 == 0 and not units % 2 == 0:
        return True


def main():
    line = read_file('../../TextFiles/2017/P3_Input_2017')

    start = line[0]
    destination = line[1]
    units = int(line[2])
    possible = ispossible(start,destination, units)
    if possible:

        print('Y')
    else:
        print('N')

if __name__ == '__main__':
    main()