def read_file(file_path):
    new_line = []
    with open(file_path, "r") as f:
        line = f.readline()
        line = line.strip()
        new_line.append(int(line))

    return new_line

def make_list(num):
    list_num = list(str(num))
    return list_num
def check_difference(num):
    list_num = make_list(num)
    difference = int(list_num[0]) - int(list_num[1])
    if int(list_num[1])+difference == int(list_num[2]) and not int(list_num[1]) == 0:
        if len(list_num) == 4:
            if int(list_num[2])+difference == int(list_num[3]):
                print(num)
                return True
            else:
                return False
        else:
            print(num)
            return True
    return False

def main():
    line = read_file('../../TextFiles/2017/P4_Input_2017')
    start = 1200
    n_line = 0
    while line[0] >= 60:
        n_line += 100
        line[0] = line[0]-60
    n_line+=line[0]
    total_arithmetic_sequences = 0
    end = start+n_line
    for i in range(start,end+1):
        if int(list(str(i))[2]) < 6:
            if int(list(str(i))[0]) == 1:
                i-=1200
                if len(list(str(i))) < 3:
                    i+=1200
                true = check_difference(i)
                if true:
                    total_arithmetic_sequences += 1
    print(total_arithmetic_sequences)

if __name__ == '__main__':
    main()