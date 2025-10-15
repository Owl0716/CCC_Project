


length = int(input(''))
rows = []
warningtape = 0
for i in range(2):
    m = []
    f = input('').split(' ')
    for j in f:
        if int(j) == 1:
            warningtape+=3
        m.append(int(j))
    rows.append(m)
for row in rows:
    print(row)
    for i in range(length-1):
        if row[i] == 1 and row[i+1] == 1:
            warningtape-=2
    for j in range(1,length):
        try:
            row.pop(j)
        except:
            break
for j in range(len(rows[0])):
    if rows[0][j] == 1 and rows[1][j] == 1:
        warningtape-=2
print(warningtape)
