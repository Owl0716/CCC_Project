players={}
players['player1']=[[3,5,7]]
players['player2']=[4,5,6]
players['player3']=[5,6,8]
players['player1'].append([4,4,4])

print(players)
for key in players.keys():
    print(key)

for key, value in players.items():
    print(value[0])