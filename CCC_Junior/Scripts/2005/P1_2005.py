
def main():
    daytime_min = int(input('Number of daytime minutes?'))
    evening_min = int(input('Number of evening minutes?'))
    weekend_min = int(input('Number of weekend minutes?'))

    price_a = 0
    price_b = 0
    daytime_min_a =daytime_min -100
    daytime_min_b =daytime_min - 250
    daytime_price_a = daytime_min_a*25
    daytime_price_b = daytime_min_b*45
    evening_price_a = evening_min*15
    evening_price_b = evening_min*35
    weekend_price_a = weekend_min*20
    weekend_price_b = weekend_min*25

    if daytime_price_a > 0:
        price_a = daytime_price_a
    if daytime_price_b > 0:
        price_b = daytime_price_b
    price_a += evening_price_a + weekend_price_a
    price_b += evening_price_b + weekend_price_b

    print(f'Plan A costs {price_a/100}')
    print(f'Plan B costs {price_b/100}')
    if price_a - price_b == 0:
        print('Plan A and B are the same price.')
    elif price_a < price_b:

        print('Plan A is cheapest')
    elif daytime_price_a > daytime_price_b:
        print(not daytime_price_a == daytime_price_b)
        print('Plan B is cheapest.')

if __name__ == '__main__':
    main()