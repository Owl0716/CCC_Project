
def main():
    quarters_num = int(input('How many quarters does Martha have in the jar?'))
    pf = int(input('How many times has the first machine been played since paying out?'))
    ps = int(input('How many times has the second machine been played since paying out?'))
    pt = int(input('How many times has the third machine been played since paying out?'))
    fp = 35
    sp = 100
    tp = 10
    turns = 0
    f=0
    while quarters_num > 0:
        pf+=1
        turns+=1
        if pf == fp:
            quarters_num+=30
            pf = 0
        quarters_num-=1

        ps+=1
        turns+=1
        if ps == sp:
            quarters_num+=60
            ps = 0
        quarters_num-=1

        pt += 1
        turns+=1
        if pt == tp:
            quarters_num += 9
            pt = 0
        quarters_num -= 1
    print(f"Martha plays {turns} times before going broke.")
if __name__ == '__main__':
    main()