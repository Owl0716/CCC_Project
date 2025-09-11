def read_file(file_path):
    with open(file_path, "r") as f:
        line = f.readline()
        line = line.strip()

    return line


def main():
    line = read_file('../../TextFiles/2016/P3_Input_2016')
    for i in range(1,len(line)-1):
        f = i+1
        if line[f] == line[-f]:
            print(line[i])




if __name__ == '__main__':
    main()