import math


def main():
    cy = int(input('Enter the current year:'))
    fy = int(input('Enter a future year:'))
    print('All positions change in year',cy)
    s = math.floor((fy - cy)/60)
    for i in range(s):
        print('All positions change in year', cy+((i+1)*60))
if __name__ == '__main__':
    main()