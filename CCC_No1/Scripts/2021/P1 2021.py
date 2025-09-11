
def read_file(text_file):
    with open(text_file,"r") as f:
        lines = f.readlines()
    return lines

def calculation(int_temp):
    P = 5 * int_temp - 400
    if int_temp >= 80 and int_temp <= 200:
        if P > 100:
            return 1,P
        elif P == 100:
            return 0,P
        else:
            return -1,P
    else:
        print("Please make temp between 80 and 200 inclusive")
def question_one():
    # 1. read file
    lines = read_file("../../TextFiles/2021/P1_Input_2021")
    int_temp = int(lines[0])
    # 2. calcuation
    result,p_cal = calculation(int_temp)
    # 3. display
    print(p_cal)
    print(result)

def question_two():
    print(1)

if __name__ == '__main__':
    question_one()