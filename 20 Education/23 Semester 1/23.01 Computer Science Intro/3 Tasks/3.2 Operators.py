def umbrella():
    clouds = input('Are there clouds today? (yes/no) ')
    rain_chance = int(input('What is the forecasted rain chance for today? (in percentage) '))

    is_umbrella = clouds == 'yes' and rain_chance > 70

    print(f'Should I take umbrella today? {is_umbrella}')


def fun_today():
    is_lesson = input('Is there a coding lesson today? (yes/no) ')
    sweets_eaten = int(input('How many sweets have you eaten today? '))

    is_fun = is_lesson == 'yes' or sweets_eaten >= 2

    print(f'Is it going to be fun today? {is_fun}')


def date():
    num = int(input('Please enter a number representing a date: '))

    year = num % 10000
    month = (num // 10000 % 100)
    day = (num // 1000000 % 100)

    print(f'The date is {day}/{month}/{year}')


def q4():
    num = int(input('Please enter a 3-digit number: '))

    dig0 = num % 10
    dig1 = num % 100 // 10
    dig2 = num // 100
    req = (dig2 + dig1) * 2 == dig0

    print(req)


def q5():
    num = int(input('Please enter a 4-digit number: '))

    dig0 = num % 10
    dig1 = num % 100 // 10
    dig2 = num // 100 % 10
    dig3 = num // 1000
    req = (dig3 + 1 == dig0) and dig1 == dig2

    print(req)


def main():
    # umbrella()
    # fun_today()
    # date()
    # q4()
    q5()

main()
