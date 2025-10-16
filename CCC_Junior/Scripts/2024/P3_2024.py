







def main():
    amount = int(input(''))
    f = []
    for j in range(amount):
        f.append(int(input('')))
    s = list(set(f))
    s.sort()
    third = s[-3]
    m = 0
    for k in f:
        if k == third:
            m+=1
    print(third,m)
if __name__ == '__main__':
    main()