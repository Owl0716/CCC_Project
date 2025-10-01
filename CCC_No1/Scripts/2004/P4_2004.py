import math

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [list(range(0,len(alphabet)))]
def read_file(file_path):
    new_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                line = line.strip()
                f = ''
                for char in line:
                    if char.isalpha():
                        f += char
                new_lines.append(f)

    return new_lines

def turnintoshifternum(shiftword):
    f = []
    for shiftletter in shiftword:
        i = alphabet.index(shiftletter)
        f.append(i)
    return f

def turnbackintononshifternum(shiftedword):
    f = []
    for shiftletter in shiftedword:

        f.append(alphabet[shiftletter])
    return f

def main():
    letterlist = []
    letternumlist = []
    n_letterlist = []

    lines = read_file('../../TextFiles/2004/P4_Input_2004')
    shifterlist = turnintoshifternum(lines[0])
    word = list(lines[1])
    value = len(shifterlist)
    # for f in range(len(lines[1])):
    print(word)
    # print(len(word),len(shifterlist),math.ceil(len(word)/len(shifterlist)))
    for p in range(len(shifterlist)):
        n_letterlist.append([])
    print(n_letterlist,'FIRST')
    print(value)
    for i in range(value):
        f=''
        for k in range(value):
            try:
                f += word[k]
            except:
                break
        if f:
            letterlist.append(f)
        else:
            break

        for i in range(value):
            try:
                word.pop(0)
            except:
                break
    try:
        letterlist.append(str(word[0]))
    except:
        print(0)
    print(letterlist)





    for z in range(len(letterlist)):
        for o in range(len(letterlist[0])):
            try:
                n_letterlist[o].append(letterlist[z][o])
                # print(letterlist[z][o])
            except:
                break
    print(n_letterlist,'n_letterlist')
    for h in n_letterlist:
        g = turnintoshifternum(h)
        letternumlist.append(g)


    for g in range(len(letterlist)):

        print(letterlist[g])
    print(letterlist, word,letternumlist,shifterlist)

    for q in range(len(shifterlist)):
        for y in range(len(letternumlist[q])):
            letternumlist[q][y] = letternumlist[q][y]+ shifterlist[q]
            if letternumlist[q][y] > 26:
                letternumlist[q][y]-=26
    letterlist = []
    for u in letternumlist:
        a = turnbackintononshifternum(u)
        letterlist.append(a)
    print(letterlist,123412341234)
    final = ''
    for b in range(len(letterlist)):
        for o in range(len(letterlist)):
            print(len(letterlist))
            # if o == len(letterlist[b])-1:
            #     letterlist.pop()
            try:
                print(letterlist[o],letterlist[o][0])
                final +=(letterlist[o][0])
                letterlist[o].pop(0)
            except:
                try:
                    break
                except:
                    break
    for r in letterlist:
        try:
            final += r[0]
        except:
            break
        print(final)
    print(letterlist)
    print(final)
if __name__ == '__main__':
    main()

