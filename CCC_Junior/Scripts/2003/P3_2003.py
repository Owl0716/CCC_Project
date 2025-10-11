

def check_square(square):
    if square == 54:
        return 19
    elif square == 90:
        return 48
    elif square == 99:
        return 77

    if square == 9:
        return 34
    elif square == 40:
        return 64
    elif square == 67:
        return 86


    return square

def main():
    square = 1
    while 1==1:
        if square == 100:
            print('You Win!')
            break
        dice = int(input('Enter sum of dice:'))

        if dice < 2 or dice > 12:
            print('You Quit!')
            break

        if square + dice < 101:

            square+=dice

        square = check_square(square)
        print(f'You are now on square {square}')

if __name__ == '__main__':
    main()
