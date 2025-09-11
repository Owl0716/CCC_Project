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
    icon = [['*','x','*'],[' ','X','X'],['*',' ','*']]
    iconsize = read_file('../../TextFiles/2012/P3_Input_2012')
    new_icon = []
    for icons in icon:
        n_icon = []
        for ico in icons:

            for i in range(iconsize[0]):
                n_icon.append(str(ico))
        for g in range(iconsize[0]):
            new_icon.append(n_icon)
    for row in new_icon:
        f= ''
        for z in row:
            f+=z
        print(f)
if __name__ == '__main__':
    main()