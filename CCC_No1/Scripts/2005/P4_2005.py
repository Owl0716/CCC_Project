def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(int(line))

    return new_lines
def create_hole(no_box_h,no_box_w,width):
    box_place = []
    for b_row in range(no_box_h):
        b = []
        for b_col in range(no_box_w):
            b.append(1)
        for g in range(width-(no_box_w*2)):
            b.append(0)
        for b_col in range(no_box_w):
            b.append(1)
        box_place.append(b)
    return box_place

def add_outer(cross):
    b= []
    for i in range(len(cross[0])):
        b.append(1)
    cross.insert(0,b)
    cross.append(b)
    for g in range(len(cross)):
        cross[g].insert(0,1)
        cross[g].append(1)
    cross[0].pop(0)
    cross[-1].pop(0)
    return cross

def move(cardinal,sub_cardinal,cross,posrow,poscol,step_num):
    for r in cross:
        c = ''
        for d in r:
            c+= f"{d:02} "
        print (c)
    print('_________________')
    cross[posrow][poscol] = step_num
    if step_num == 0:
        return posrow,poscol,cross
    if cardinal == 'Left' and poscol - 1 > -1 and cross[posrow][poscol - 1] == 0:
        return move(cardinal, sub_cardinal, cross, posrow, poscol - 1, step_num - 1)

    elif cardinal == 'Right' and posrow+1 < len(cross)-2 and cross[posrow][poscol+1] == 0:
        return move(cardinal, sub_cardinal, cross, posrow, poscol+1, step_num-1)

    elif cardinal == 'Up' and posrow - 1 < len(cross) - 2 and cross[posrow - 1][poscol] == 0:
        return move(cardinal, sub_cardinal, cross, posrow - 1, poscol, step_num - 1)

    elif cardinal == 'Down' and posrow + 1 > -1 and cross[posrow + 1][poscol] == 0:
        return move(cardinal, sub_cardinal, cross, posrow + 1, poscol, step_num - 1)
    else:
        if sub_cardinal == 'Left' and poscol - 1 > -1 and cross[posrow][poscol - 1] == 0:
            return move(cardinal, sub_cardinal, cross, posrow, poscol-1, step_num - 1)

        elif sub_cardinal == 'Right' and posrow + 1 < len(cross) - 2 and cross[posrow][poscol + 1] == 0:
            return move(cardinal, sub_cardinal, cross, posrow, poscol + 1, step_num - 1)

        elif sub_cardinal == 'Up' and posrow - 1 < len(cross) - 2 and cross[posrow -1][poscol] == 0:
            return move(cardinal, sub_cardinal, cross, posrow-1, poscol, step_num - 1)

        elif sub_cardinal == 'Down' and posrow + 1 > -1 and cross[posrow+1][poscol] == 0:
            return move(cardinal, sub_cardinal, cross, posrow+1, poscol, step_num - 1)
        else:
            if not cross[posrow -1][poscol] == 0 and not cross[posrow+1][poscol]  == 0 and not cross[posrow][poscol + 1]  == 0 and not cross[posrow][poscol - 1] == 0:
                return posrow, poscol, cross
            elif cardinal == 'Up' and sub_cardinal == 'Right':
                return move('Right', 'Down', cross, posrow, poscol, step_num)
            elif cardinal == 'Right' and sub_cardinal == 'Down':
                return move('Down', 'Left', cross, posrow, poscol, step_num)
            elif cardinal == 'Down' and sub_cardinal == 'Left':
                return move('Left', 'Up', cross, posrow, poscol, step_num)
            elif cardinal == 'Left' and sub_cardinal == 'Up':
                return move('Up', 'Right', cross, posrow, poscol, step_num)

def main():

    lines = read_file('../../TextFiles/2005/P4_Input_2005')
    width = lines[0]
    height = lines[1]
    no_box_w = lines[2]
    no_box_h = lines[3]
    steps = lines[4]
    cardinal = 'Up'
    sub_cardinal = 'Right'

    cross = []
    box_place = create_hole(no_box_h, no_box_w, width)
    cross += box_place

    for row in range(height-(no_box_h*2)):
        r = []
        for col in range(width):
            r.append(0)
        cross.append(r)

    box_place = create_hole(no_box_h, no_box_w, width)
    cross += box_place
    cross = add_outer(cross)
    row,col,cross = move(cardinal,sub_cardinal,cross,1,no_box_w+1,steps)
    print(col)
    print(row)
if __name__ == '__main__':
    main()