

def main():
    lines = int(input('Enter w: '))
    message = ['WELCOME','TO','CCC','GOOD','LUCK','TODAY']
    used = []
    l1 = ''
    l2 = ''
    l3 = ''
    l4 = ''

    print(l2)
    print(l3)
    print(l4)
    if not message == []:
        l1,used = do_stuff(l1, lines, message, used)
        print(l1)
    if not message == []:
        l2,used = do_stuff(l2, lines, message, used)
        print(l2)
    if not message == []:
        l3,used = do_stuff(l3, lines, message, used)
        print(l3)
    if not message == []:
        l4,used = do_stuff(l4, lines, message, used)
        print(l4)
    # for i in range(100):
    #     if not l1[-1] == '.':
    #         break
    print(len(l1),len(l2),len(l3),len(l4))

def do_stuff(thing, lines, message, used):
    dots = 0
    for i in message:
        if not len(thing) + len(i) > lines:
            thing += i
            thing += ' '
            dots+=1
            used.append(i)
        elif not len(thing) > lines:
            thing += ' '
            dots+=1
    for g in used:
        message.remove(g)
    # thing = thing.replace(' ', '.')
    diff = abs(lines - len(thing))
    thing = thing.split()
    if lines > len(thing):
        dots += diff
    else:
        dots -= diff
    print(dots)
    if not len(thing) == 1:
        while dots > 0:
            for f in range(len(thing)-1):
                thing[f]+='.'
                dots-=1
                if dots < 1:
                    break
    else:
        for i in range(dots):
            thing.append('.')
    thingstr = ''
    for i in thing:
        thingstr += i
    return thingstr,[]


if __name__ == '__main__':
    main()