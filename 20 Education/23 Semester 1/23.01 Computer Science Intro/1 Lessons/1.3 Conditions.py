def q1():
    temperature = int(input('Enter the temperature in Celsius: '))

    if temperature < 11:
        print('Its going to rain')


def q2():
    temperature = int(input('Enter the temperature in Celsius: '))
    is_cloudy = input('Are there clouds today? (y/n) ')

    if temperature < 11 and is_cloudy == 'y':
        res = 'Its going to rain'
    else:
        res = 'Its NOT going to rain'

    print(res)

def q2v2(): # More user-friendly
    temperature = int(input('Enter the temperature in Celsius: '))
    res = 'Its NOT going to rain'

    if temperature < 11:
        is_cloudy = input('Are there clouds today? (y/n) ')
        if is_cloudy == 'y':
            res = 'Its going to rain'

    print(res)

def q3():
    num = int(input('Enter a number: '))

    if 10 > num // 10 > 0:
        res = 'This is a 2-digit number'
    elif 10 > num // 1000 > 0:
        res = 'This is a 4-digit number'
    else:
        res = 'This is NOT a 2 or 4 digits number'

    print(res)


def q4():
    rooms_quantity = int(input('How many rooms are there in your apartment? '))

    if rooms_quantity < 3 or rooms_quantity > 5:
        print('Invalid input')
        exit()

    if rooms_quantity == 3:
        rent = 120
    elif rooms_quantity == 4:
        rent = 150
    elif rooms_quantity == 5:
        is_duplex = input('Is your apartment a duplex? (y/n) ')
        if is_duplex == 'y':
            rent = 200
        else:
            rent = 180

    print(f'Your monthly rent is: {rent}')


def q5():
    age = int(input('What is the age of your child? '))
    height = int(input('What is the height of your child? '))

    if age < 0 or age > 8 or height < 40 or height > 140:
        print('Invalid input')
        exit()

    if age >= 0 and age < 3:
        calories = 700
    else:
        if height >= 40 and height <= 100:
            calories = 900
        else:
            calories = 1200

    print(f'Your child needs to consume {calories} calories')


def main():
    # q1()
    # q2()
    # q2v2()
    q3()
    # q4()
    # q5()


main()
