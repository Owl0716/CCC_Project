




def main():
    m = int(input('Enter m:'))
    n = int(input('Enter n:'))
    if m > 9:
        m_list = list(range(1,10))
    else:
        m_list = list(range(1,m+1))
    if n > 9:
        n_list = list(range(1,10))
    else:
        n_list = list(range(1,n+1))
    ways = 0
    if len(n_list) >= len(m_list):
        n_list.reverse()
        for s in range(len(m_list)):
            if m_list[s]+n_list[0] == 10:
                print(len(m_list)-s)
    else:
        m_list.reverse()
        for s in range(len(n_list)):
            if n_list[s]+m_list[0] == 10:
                print(len(n_list)-s)
if __name__ == '__main__':
    main()