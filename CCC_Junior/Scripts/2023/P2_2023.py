f = int(input(''))
s = 0
for j in range(f):
    k = input('')
    if k == 'Poblano':
        s+=1500
    if k == 'Mirasol':
        s+=6000
    if k == 'Serrano':
        s+=15500
    if k == 'Cayenne':
        s+=40000
    if k == 'Thai':
        s+=75000
    if k == 'Habanero':
        s+=125000
print(s)
