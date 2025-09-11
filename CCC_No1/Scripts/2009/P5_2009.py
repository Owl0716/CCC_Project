
friends = {
    1:[6],
    2:[6],
    3:[4,6,5,15],
    4:[3,6,5],
    5:[4,3,6],
    6: [1,2,3,4,5,7],
    7: [6,8],
    8: [7,9],
    9: [8,10,12],
    10: [9,11],
    11: [10, 12],
    12: [9,11,13],
    13: [12,14,15],
    14: [13],
    15: [13,3],
    16: [18,17],
    17: [16,18],
    18: [16,17]
}
import copy
def rules(text):
    person = 0
    friend = 0
    rule = text[0]
    if len(text) >= 2:
        person = int(text[1])
    if len(text) >= 3:
        friend = int(text[2])
    if rule == 'i':
        if not friends.get(person):
            friends[person] = []
        if not friends.get(friend):
            friends[friend] = []
        if not person in friends[friend]:
            friends[person].append(friend)
            friends[friend].append(person)
    elif rule == 'd':
        if person in friends[friend]:
            friends[person].remove(friend)
            friends[friend].remove(person)
    elif rule == 'n':
        print(len(friends[person]))
    elif rule == 'f':
        f = 0
        for friendsa in friends[person]:
            f += len(friends[friendsa])-1
        print(f)
    elif rule == 's':
        visited = []

        fastest = find_shortest_path(visited,person,friend)
        if fastest == None:
            print('Not connected')
        else:
            print(fastest)
    elif rule == 'q':
        return True

def find_shortest_path(visited,person,friend):
    visited = visited + [person]
    if friend in visited:
        return len(visited)-1
    shortest = None
    for p in friends[person]:
        if p not in visited:
            dist  = find_shortest_path(visited, p, friend)
            if dist is not None:
                if shortest is None or dist < shortest:
                    shortest = dist
    return shortest

def main():
    quit = False
    while not quit == True:
        text = input()
        text = text.split()
        quit = rules(text)

if __name__ == '__main__':
    main()