import math


def main():
    f = []
    value = 1
    day = int(input('Enter day:'))
    amount_of_days = int(input('Enter the number of days in the month:'))
    print('Sun Mon Tue Wed Thr Fri Sat')
    for j in range(day-1):
        f.append('   ')
        f.append(' ')
    for m in range(5):
        for k in range(7 - int(len(f)/2)):
            f.append(f'   ')
            g = len(str(value))
            f[-1] = f[-1][:-g]
            f[-1] = f[-1]+str(value)
            f.append(' ')
            # if value == day:
            #     print(value,day)
            #     break
            if value >= amount_of_days:
                break
            value+=1
        k = ''
        for r in f:
            k += str(r)
        f = []
        print(k)
if __name__ == '__main__':
    main()