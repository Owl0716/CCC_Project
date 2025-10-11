import math


def main():
    tine_length = int(input('Enter tine length:'))
    tine_spacing = int(input('Enter tine spacing:'))
    handle_length = int(input('Enter handle length:'))
    for length in range(tine_length):
        point = ''
        for points in range(3):
            point+='*'
            for i in range(tine_spacing):
                point+=' '
        print(point)
    k=''
    for j in range(len(point)-tine_spacing):
        k+='*'
    print(k)
    y = ''
    for m in range(tine_spacing+1):
        y+=' '
    y+='*'
    for n in range(handle_length):
        print(y)

if __name__ == '__main__':
    main()