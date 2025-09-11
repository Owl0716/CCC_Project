def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)
    return new_lines
def make_list(string):
    nlist = string.split(' ')
    new_list =[]
    for i in range(len(nlist)):
        if not nlist[i] == ' ':
            new_list.append(int(nlist[i]))
    new_list.sort()
    return new_list
def check_duplicate(num,lists):
    counter=0
    for numb in lists:
        if int(numb) == int(num):
            counter+=1
    return counter,num
def main():
    lines = read_file('../../TextFiles/2017/P5_Input_2017')
    org_string = lines[1]
    length = 0
    num_of_different_heights = 0
    new_list = make_list(org_string)
    num_list = []
    wall_height = []
    for f in range(len(new_list)):
        for i in range(1,len(new_list) - f):
            wall_height.append(new_list[f]+new_list[i+f])
    for i in range(len(wall_height)):
        new_counter,num = check_duplicate(wall_height[i],wall_height)
        if length > 1:
            num_of_different_heights = 1
        if new_counter >= length:
            length = new_counter
            if not num in num_list:
                num_list.append(num)
                num_of_different_heights+=1
    test_num = num_list[-1]
    l = 0
    for z in range(len(new_list)):
        for y in range(1, len(new_list) - z):
            if new_list[z] + new_list[y + z] == test_num:
                new_list[z] = -5000
                new_list[y + z] = -5000
                l +=1
    print(l,num_of_different_heights)
if __name__ == '__main__':
    main()