def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines

def rule(rule_convert, rule, strings):
    if rule_convert in strings[:len(rule_convert)]:
        strings = list(strings)
        strings[:len(rule_convert)] = rule

    return strings
def futures(rule_convert, rule, strings):
    strings = list(strings)
    strings[:len(rule_convert)] = rule
    new_strings = ''
    for char in strings:
        new_strings += char

    return new_strings


def temp_name(rule_1_convert,rule_2_convert,rule_3_convert,rule_1,rule_2,rule_3,times,string,end,existing,start):

    strings = string
    new_strings = ''
    future = []
    s = futures(rule_1_convert,rule_1,strings)
    future.append(s)
    s = futures(rule_2_convert,rule_2,strings)
    future.append(s)
    s = futures(rule_3_convert,rule_3,strings)
    future.append(s)
    # print(f"future {future}")

    print()
    print(f"existing {existing}")
    print()

    if not future[0] in existing:
        strings = rule(rule_1_convert,rule_1,strings)
    if not future[1] in existing:
        strings = rule(rule_2_convert,rule_2,strings)
    if not future[2] in existing:
        strings = rule(rule_3_convert,rule_3,strings)


    for char in strings:
        new_strings += char
    existing.append(new_strings)
    if times == 0 and new_strings == end:

        return new_strings,existing
    elif times == 0 or new_strings == end:
        return temp_name(rule_1_convert, rule_2_convert, rule_3_convert, rule_1, rule_2, rule_3, times-1, start, end,existing,start)
    else:
        return temp_name(rule_1_convert, rule_2_convert, rule_3_convert, rule_1, rule_2, rule_3, times-1, new_strings, end,existing,start)

def main():
    lines = read_file('../../TextFiles/2019/P5_Input_2019')
    rule_1_convert ,rule_1 = lines[0].split(' ')
    rule_2_convert ,rule_2 = lines[1].split(' ')
    rule_3_convert ,rule_3 = lines[2].split(' ')

    temp = lines[3]
    times,string ,end = temp.split(' ')
    existing = []
    string,existing = temp_name(rule_1_convert,rule_2_convert,rule_3_convert, rule_1,rule_2,rule_3,int(times)-1, string, end,existing,string)

if __name__ == '__main__':
    main()