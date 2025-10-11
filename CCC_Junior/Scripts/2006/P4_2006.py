tasks = {
#task:what you must do before
    1:[2],
    2:[],
    3:[],
    4:[3,1],
    5:[3],
    6:[],
    7:[1]
}
def do_task():
    for task in tasks:
        if not tasks[task]:
            print(task)
            tasks.pop(task)
            return task
    return None
def delete_all_ts(t):
    for task in tasks:
        if t in tasks[task]:
            tasks[task].remove(t)
def main():
    task_placement = ''
    previous = 10
    current = 10
    f=False
    while not previous == 0 and not current == 0:
        current = int(input())

        if not previous == 10:
            try:
                tasks[current].append(previous)
                current = 10
                previous = 10
            except:
                continue
        else:
            previous = current
    print(previous,current)
    for i in range(100):
        if not tasks:
            f = True
            break
        print(tasks)
        t = do_task()
        if t:
            delete_all_ts(t)
            task_placement +=f'{t} '
    if f:
        print(task_placement)
    else:
        print('Cannot complete these tasks. Going to bed.')
if __name__ == '__main__':
    main()