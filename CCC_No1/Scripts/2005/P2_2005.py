

def factorization(num):
    f = 0
    for i in range(1,num+1):
        # print(num%i)
        if num % i == 0:
            f+=1
    return f


def main():
    ll = int(input('Enter lower limit of range'))
    orL = ll
    ul = int(input('Enter upper limit of range'))
    f=0
    while not ll == ul:
        factors = factorization(ll)

        if factors == 4:
            f+=1

        ll+=1
    print(f'The number of RSA numbers between {orL} and {ul} is {f}')
if __name__ == '__main__':
    main()