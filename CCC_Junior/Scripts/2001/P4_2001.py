import math





def main():
    start_value = int(input('Start value:'))
    end_value = int(input('End value:'))
    value = start_value
    difference = abs(start_value-end_value)
    length = math.ceil(math.sqrt(difference))
    middle = int(math.ceil(length/2))-1
    current_row = middle
    current_col = middle
    print(middle)
    spiral = create_spiral(length)
    distance = 1
    direction = 'down'

    spiral[current_row][current_col] = value
    for i in range(difference):
        current_row,current_col,value = move(current_row,current_col,value, distance, direction,spiral,end_value)
        if value == 'stop':
            break

        if direction == 'up':
            direction = 'left'
            distance-=1
        elif direction == 'down':
            direction = 'right'
            distance-=1
        elif direction == 'left':
            direction = 'down'
        elif direction == 'right':
            direction = 'up'
        if direction == 'up' or 'down':
            distance+=1

    for row in spiral:
        b= ''
        for j in row:
            j = str(j).zfill(2)
            b += str(j)
            b+= ' '
        print(b)

def move(current_row,current_col,value,distance,direction,spiral,end_value):
    for d in range(distance):
        value+=1
        if direction == 'up':
            current_row-=1
        elif direction == 'down':
            current_row+=1
        elif direction == 'left':
            current_col-=1
        elif direction == 'right':
            current_col+=1
        spiral[current_row][current_col] = value
        if value == end_value:
            value = 'stop'
            break
    return current_row,current_col,value
def create_spiral(length):
    spiral = []
    for rows in range(length):
        row = []
        for cols in range(length):
            row.append('  ')
        spiral.append(row)
    return spiral


if __name__ == '__main__':
    main()