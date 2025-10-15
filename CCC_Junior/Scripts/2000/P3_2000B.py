
def main():
    quarters_num = int(input('How many quarters does Martha have in the jar?'))
    played_on_first_machine = int(input('How many times has the first machine been played since paying out?'))
    played_on_second_machine = int(input('How many times has the second machine been played since paying out?'))
    played_on_third_machine = int(input('How many times has the third machine been played since paying out?'))
    first_payout = 35
    second_payout = 100
    third_payout = 10
    turns = 0
    f=0
    while quarters_num > 0:
        played_on_first_machine+=1
        turns+=1
        if played_on_first_machine == first_payout:
            quarters_num+=30
            played_on_first_machine = 0
        quarters_num-=1

        if quarters_num==0:
            break

        played_on_second_machine+=1
        turns+=1
        if played_on_second_machine == second_payout:
            quarters_num+=60
            played_on_second_machine = 0
        quarters_num-=1

        if quarters_num==0:
            break

        played_on_third_machine += 1
        turns+=1
        if played_on_third_machine == third_payout :
            quarters_num += 9
            played_on_third_machine = 0
        quarters_num -= 1

    print(f"Martha plays {turns} times before going broke.")
if __name__ == '__main__':
    main()