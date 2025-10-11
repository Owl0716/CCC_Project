possible_result = ['W','L','T']
possibilities =[]
for i in possible_result:
    for j in possible_result:
        for k in possible_result:
            for m in possible_result:
                possibilities.append([i,j,k,m])
for i in possible_result:
    for j in possible_result:
        for k in possible_result:
                possibilities.append([i,j,k])
print(f"possibilities {possibilities}")
print(f"count is: {len(possibilities)}")