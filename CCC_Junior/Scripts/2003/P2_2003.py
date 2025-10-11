import math


def factorization(num):
    factorlist = []
    for i in range(1,num+1):
        if num % i == 0:
            factorlist.append(i)
    return factorlist


def main():
    while 1==1:
        picture_num = int(input('Enter number of pictures:'))
        if picture_num == 0:
            break
        factorlist = factorization(picture_num)
        while len(factorlist) > 2:
            factorlist.pop(0)
            factorlist.pop(-1)
        dimensions = f'{factorlist[0]} x {factorlist[-1]}'
        p = (factorlist[0]*2)+(factorlist[-1]*2)
        print(f'Minimum perimeter is {p} with dimensions {dimensions}')

if __name__ == '__main__':
    main()