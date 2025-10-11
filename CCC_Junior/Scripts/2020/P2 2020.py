def read_file(file_path):
    new_lines = []
    with open(file_path,"r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip() == '':
                new_lines.append(int(line.strip()))

    return new_lines
def infect(people,infected_per_person,needed_days,total_people):
    print(people)
    previous_people = people
    people *=infected_per_person+1
    people -= previous_people
    needed_days += 1

    return needed_days, people,total_people+people
def main():
    lines = read_file("../../TextFiles/2020/P2_Input_2020")
    quota = lines[0]
    starting_people = lines[1]
    infected_per_person = lines[2]
    needed_days = 0
    people = starting_people
    total_people = 1
    while not total_people > quota:
        needed_days,people,total_people = infect(people,infected_per_person,needed_days,total_people)
        print(total_people)
    print(people)
    print(needed_days)


if __name__ == '__main__':
    main()