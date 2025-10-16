import math
def jasonisdumb1(num):
    m = 0
    for j in range(1,num+1):
        if num % j == 0:
            k = math.sqrt(j)
            if k.is_integer():
                m+=1
    return m
m = jasonisdumb1(int(input('How dumb is jason?:')))
print(m)