def printFirstLine(day):
    result = ""
    spaces = "    "*(day-1)
    result += spaces
    for i in range(1,7-day+2):
        result += "  "+str(i)+" "
    print(result)

def printRestLine(start,end):
    result=""
    for i in range(start+1, end+1):
        # print(i-start)
        result +=f"{i:>3} "
        if (i-start) %7 ==0 and i!=start:
            print(result)
            result=""
    print(result)

def main():
    # day = int(input('Enter day:'))
    day = 2
    # amount_of_days = int(input('Enter the number of days in the month:'))
    amount_of_days = 31
    print('Sun Mon Tue Wed Thr Fri Sat')
    printFirstLine(day)
    printRestLine(8-day,amount_of_days)
if __name__ == '__main__':
    main()