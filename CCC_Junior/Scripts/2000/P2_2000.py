num = {
    1:1,
    6:9,
    8:8,
    9:6,
    0:0

}
import math
def main():
    lowest_num = int(input('Enter the lower bound of the interval:'))
    highest_num = int(input('Enter the upper bound of the interval:'))
    m=0
    for i in range(lowest_num,highest_num+1):
        new_num = ''
        for j in str(i):
            try:
                q = int(j)
                new_num+=str(num[q])
            except:
                break

        new_num = list(new_num)
        new_num.reverse()
        n = ''
        for l in new_num:
            n+= l
        if not n == '':
            new_num_int = int(n)
            if i == new_num_int:
                m+=1
    print('The number of rotatable numbers is:')
    print(m)

if __name__ == '__main__':
    main()