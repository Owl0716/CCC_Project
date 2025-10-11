









def main():
    costs = []
    t = []
    # start =
    costs.append(int(input('Cost of PINK tickets:')))
    costs.append(int(input('Cost of GREEN tickets:')))
    costs.append(int(input('Cost of RED tickets:')))
    costs.append(int(input('Cost of ORANGE tickets:')))
    goal = int(input('How much must be raised with ticket sales?'))
    print(costs,goal)
    for i in costs:
        for k in costs:
            if i+k == goal :
                s = []
                s = i,k
                sorted(s)
                print(s)
                # t.append(i,k)

                print(i+k,i,k)


if __name__ == '__main__':
    main()


