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
    starting = read_file('../../TextFiles/2011/P3_Input_2011')
    t = 1
    while not starting[t-1] < starting[t]:
        diff = starting[t-1] - starting[t]
        starting.append(diff)
        t+=1
    print(t+1)
if __name__ == '__main__':
    main()