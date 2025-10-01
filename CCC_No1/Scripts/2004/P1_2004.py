import math


def main():
    tiles = int(input('Number of tiles?'))
    s_l = math.sqrt(tiles)
    print(f'The largest square has side length {math.floor(s_l)}.')

if __name__ == '__main__':
    main()