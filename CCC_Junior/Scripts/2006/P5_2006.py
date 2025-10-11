def read_file(file_path):

    with open(file_path, "r") as f:
        line = f.readline()
    return line


def main():
    line = read_file('../../TextFiles/2006/P5_Input_2006')
    line = line.split(' ')
    config = line[0]
    steps = int(line[1])
if __name__ == '__main__':
    main()