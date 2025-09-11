dic = {}
def store(type,value,amount):
    if not value in dic:
        dic[value] = []
    try:
        int(amount)
    except:
        amount = dic[amount][-1]
    amount = int(amount)
    if type == 1:
        dic[value].append(amount)
    elif type == 2:
        print(dic[value][-1])
    elif type == 3:
        dic[value].append(amount+ dic[value][-1])
    elif type == 4:
        dic[value].append(amount * dic[value][-1])
    elif type == 5:
        dic[value].append(dic[value][-1] - amount)
    elif type == 6:
        dic[value].append(dic[value][-1] / amount)
def main():
    lines = '0'
    while not lines[0] == '7':
        lines =input()
        if len(lines) == 5:
            store(int(lines[0]),lines[2],lines[4])
        elif len(lines) == 3:
            store(int(lines[0]),lines[2],0)
if __name__ == '__main__':
    main()