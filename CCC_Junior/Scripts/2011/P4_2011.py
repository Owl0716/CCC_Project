def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines

def drill_hole(direction,spaces,current_x,current_y,ground):
    new_x = current_x
    new_y = current_y
    if direction == 'd':
        new_y -=spaces
        spaces *=-1
    elif direction == 'u':
        new_y+=spaces
    elif direction == 'l':
        new_x-=spaces
        spaces *=-1
    elif direction == 'r':
        new_x+=spaces
    elif direction =='q':
        stop = True
        return [0,0],ground,stop
    if new_x == current_x:

        for x in range(1,abs(spaces)+1):
            if len(str(spaces).replace('-','he')) == len(str(spaces)):
                ground[abs(current_y+x)][current_x+200] += 1

            else:
                ground[abs(current_y-x)][current_x+200] += 1

    else:

        for y in range(1,abs(spaces)+1):
            if len(str(spaces).replace('-','--')) == len(str(spaces)):
                ground[abs(current_y)][current_x+200+y] += 1

            else:
                ground[abs(current_y)][current_x+200-y] += 1

    new_place = [new_x,new_y]
    return new_place,ground,False

def main():
    lines = read_file('../../TextFiles/2011/P4_Input_2011')
    start = [['d', '3'],['r','3'],['d', '2'],['r', '2'],['u', '2'],['r', '2'],['d', '4'],['l', '9'],['u' ,'2']]
    current_place = [0,1]
    n_start = []
    ground = []
    for r in range(len(lines)):
        l = lines[r].split(' ')
        n_start.append(l)
    lines = n_start
    for q in lines:
        start.append(q)
    for f in range(200):
        row = []
        for i in range(400):
            row.append(0)
        ground.append(row)
    stop = False
    for g in range(len(start)):
        direction = start[g][0]
        spaces = start[g][1]
        spaces = int(spaces)

        x =current_place[0]
        y =current_place[1]
        current_place,ground,stopq = drill_hole(direction,spaces,x,y,ground)

        if 0+x < 0:
            x = abs(x)-1
            x *= -1
        else:
            x = abs(x)+1
        if 0+y < 0:
            y = abs(y)+1
            y *= -1
        else:
            y = y+1
        if stop:
            print(x, y,'DANGER')
            break
        elif stopq:
            print(x, y,'safe')
            break
        elif g > 9:
            print(x, y,'safe')
        for row in range(len(ground)):
            if 2 in ground[row]:
                stop = True
                break
if __name__ == '__main__':
    main()