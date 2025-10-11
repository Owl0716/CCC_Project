def read_file(file_path):

    new_lines = []

    with open(file_path,"r") as f:

        lines = f.readlines()

        for line in lines:
            new_lines.append(line.strip())

    return new_lines

def bids(bidder_num,lines):

    highest_bid = 0
    bidder = ""

    for i in range(1,bidder_num*2+1,2):
        if int(lines[i+1]) > highest_bid:
            highest_bid = int(lines[i+1])
            bidder = lines[i]

    return bidder
def main():
    lines = read_file("../../TextFiles/2021/P2_Input_2021")
    bidder_num = int(lines[0])
    bidder = bids(bidder_num,lines)
    print(bidder)


if __name__ == '__main__':
    main()