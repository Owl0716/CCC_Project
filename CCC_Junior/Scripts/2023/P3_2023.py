people = int(input(''))
k = []
u = ''
most = 0
king = []
for j in range(people):
    k.append(input(''))
for i in range(len(k[0])):
    thing = 0
    y = []
    q = True
    for m in range(people):
        y.append(k[m][i])
    for a in y:
        if a == 'Y':
            thing +=1
    king.append(thing)
    if most < thing:
        most = thing
j = ''
for y in range(len(king)):
    if king[y] == most:
        j+= f'{y+1},'
print(j[:-1])