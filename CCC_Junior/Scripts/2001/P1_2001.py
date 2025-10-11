import math


def main():
    height = int(input('Enter height:'))
    width = height*2

    f = []
    i = []
    s=[]
    for j in range(width):
        f.append(' ')
    for m in range(height+1):
        f[m],f[-(m+1)] = '*','*'
        if m % 2 == 0:
            i += f
    s +=i
    for r in range(int(len(i)/height)):
        if s:
            o = ''
            for m in s[:width]:
                o+=m
            print(o)
            for j in range(width):
                s.pop(0)
    if not height % 2 == 0:
        i = i[:-width]
    for r in range(int(len(i)/height)):
        if i:
            o = ''
            for m in i[-width:]:
                o+=m
            print(o)
            for j in range(width):
                try:
                    i.pop(-1)
                except:
                    break
if __name__ == '__main__':
    main()