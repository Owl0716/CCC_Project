
def main():
    weight = float(input('Enter weight:'))
    height = float(input('Enter height:'))

    real_weight = float(weight/(height**2))
    if real_weight > 25:
        print('Overweight')
    elif real_weight < 18.5:
        print('Underweight')
    else:
        print('Normal weight')

if __name__ == '__main__':
    main()