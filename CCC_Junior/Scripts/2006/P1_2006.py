def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(int(line))

    return new_lines
def main():
    b = [461,431,420,0]
    dr = [130,160,118,0]
    s = [100,57,70,0]
    de = [167,266,75,0]
    amount = 0
    lines = read_file('../../TextFiles/2007/P1_Input_2007')
    print('Welcome to Chip’s Fast Food Emporium')
    burger_num = int(input('Please enter a burger choice:'))-1
    side_order_num = int(input('Please enter a side order choice:'))-1
    drink_num = int(input('Please enter a drink choice:'))-1
    dessert_num = int(input('Please enter a dessert choice:'))-1

    amount = b[burger_num]+s[side_order_num]+dr[drink_num]+de[dessert_num]
    print(f'Your total Calorie count is {amount}.')

if __name__ == '__main__':
    main()