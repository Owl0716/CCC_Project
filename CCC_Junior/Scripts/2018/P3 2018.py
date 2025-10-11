def read_file(file_path):
    new_lines = ''
    with open(file_path, "r") as f:
        lines = f.readline()
        new_lines = lines

    return new_lines

def distance(cities):
    total_distances = []
    for i in range(len(cities)):
        distances = []
        dist = ''
        for city in cities:
            distances.append(abs(city-cities[i]))

        for d in distances:
            dist += f" {str(d)}"
        total_distances.append(dist)

    return total_distances


def main():
    lines = read_file('../../TextFiles/2018/P3_Input_2018')
    line = lines.split(' ')
    city1 = 0
    city2 = int(line[0])
    city3  = int(line[1]) + city2
    city4 = int(line[2]) + city3
    city5  = int(line[3]) + city4
    cities = [city1,city2,city3,city4,city5]
    total_distances = distance(cities)

    for distances in total_distances:
        print(distances)

if __name__ == '__main__':
    main()