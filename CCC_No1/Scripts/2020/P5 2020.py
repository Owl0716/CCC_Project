def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                new_lines.append(line.strip())

    return new_lines

def split_room(room):
    new_room = []
    for row in room:
        new_row = []
        for r in row.split():
            new_row.append(int(r))
        new_room.append(new_row)
    return new_room


def escape_room(rows,cols,room,start,finish):
    previous_pos_num = finish
    for i in range(rows*cols):
        for r in range(len(room)):
            if previous_pos_num in room[r]:

                # print(previous_pos_num)
                pos = room[r].index(previous_pos_num)+1
                # print(rows,pos)
                row = r+1

                previous_pos_num = row*pos
                # print(previous_pos_num)
                # print(r)
        if previous_pos_num == start:
            # print(previous_pos_num)
            break


def main():
    lines = read_file('../../TextFiles/2020/P5_Input_2020')
    rows = int(lines[0])
    cols = int(lines[1])
    room = lines[2:]
    room = split_room(room)
    start = room[0][0]
    finish = room[rows-1][cols-1]
    #work backwards
    escape_room(rows,cols,room,start,finish)
if __name__ == '__main__':
    main()