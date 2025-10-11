def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                new_lines.append(line)

    return new_lines
players = {1: [],
           2: [],
           3: [],
           4: []}
def build_existing_game(lines):
    # goal: for example: "TLT-W-"
    p1 = 0
    p2 = 0
    for game in lines:
        p1 = int(game[0])
        p2 = int(game[2])
        score1 = int(game[4])
        score2 = int(game[6])
        if score1 > score2:
            players[p1].append('W')
            players[p2].append('L')
        elif score2 > score1:
            players[p2].append('W')
            players[p1].append('L')
        else:
            players[p2].append('T')
            players[p1].append('T')
import  random as rand
def remaining(remaining_games):
    possiblities = []
    possibility=3
    for i in range(remaining_games-1):
        possibility *=3
    c= 0
    while not len(possiblities) == possibility:
        s = ''
        for i in range(remaining_games):
            f = rand.randint(1,3)
            if f == 1:
                s += 'W'
            elif f == 2:
                s += 'L'
            else:
                s +='T'

        possiblities.append(s)
        possiblities = list(set(possiblities))
        c+=1
    possiblities.sort()
    return possiblities
import copy
def check(remaining_matches,outcomes,fav_num):
    favs = 0
    for f in outcomes:
        i = 0
        p = copy.deepcopy(players)

        for match in remaining_matches:

            p1 = match[0]
            p2 = match[1]
            outcome = f[i]
            p[p1].append(outcome)
            if outcome == 'W':
                p[p2].append('L')
                # print(f"winner of {f} {p1}")
            elif outcome == 'L':
                p[p2].append('W')
                # print(f"winner of {f} {p2}")
            else:
                p[p2].append('T')
            # players[p1].append()
            i+=1
        p1wins = p[1].count("W")
        p2wins = p[2].count("W")
        p3wins = p[3].count("W")
        p4wins = p[4].count("W")
        p1ties  = p[1].count("T")
        p2ties  = p[2].count("T")
        p3ties  = p[3].count("T")
        p4ties = p[4].count("T")
        p1score = (p1wins*3)+(p1ties)
        p2score = (p2wins*3)+(p2ties)
        p3score =(p3wins)+(p3ties)
        p4score =(p4wins)+(p4ties)
        wins =[p1score,p2score,p3score,p4score]
        winner = max(wins)
        print(winner)
        if p1score == winner:
            winner = 1
        elif p2score == winner:
            winner = 2
        elif p3score == winner:
            winner = 3
        else:
            winner = 4
        if winner == fav_num:
            favs += 1
    print(players)

    return favs

def main():
    matches = [[1,3],[3,4],[2,4],[1,2],[2,3],[1,4]]
    lines = read_file('../../TextFiles/2013/P5_Input_2013')
    favorite_player = int(lines[0])
    no_games = int(lines[1])

    lines[2:].sort()
    remaining_games = 6 - len(lines[2:])
    remaining_matches = matches[abs(6-remaining_games):]
    build_existing_game(lines[2:])
    outcomes = remaining(remaining_games)
    favs = check(remaining_matches,outcomes,favorite_player)
    print(favs)
if __name__ == '__main__':
    main()