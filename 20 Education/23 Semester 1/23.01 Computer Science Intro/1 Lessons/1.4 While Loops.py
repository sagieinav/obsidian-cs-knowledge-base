def q1v1():
    num = int(input('Please enter a number: '))

    dig_count = 1
    while num >= 10 or num <= -10:
        dig_count += 1
        num //= 10

    print(f'Your number has {dig_count} digit/s')

def q1():
    num = (
        int(input('Please enter a number: ')))

    dig_count = 0
    while num != 0:
        dig_count += 1
        num //= 10
    dig_count = dig_count if dig_count != 0 else 1


    print(f'Your number has {dig_count} digit/s')

def q2():
    even_nums_count = 0
    while even_nums_count < 5:
        num = int(input('Enter numbers, the program will stop when 5 even numbers have been entered: '))
        if num % 2 == 0:
            even_nums_count += 1


def q3():
    num = int(input('Enter numbers, the program will stop when a 3-digit number has been entered: '))
    while num > 999 or num < 100:
        num = int(input('Enter numbers, the program will stop when a 3-digit number has been entered: '))


def q4():
    condition = False
    while not condition:
        num = int(input('Enter numbers, the program will stop when a 2-digit number with equal digits has been entered: '))
        condition = num < 100 and num > 9 and num % 10 == num // 10


def q5():
    num1 = int(input('Enter a number: '))

    num2 = 0
    num2_dig_pos = 0

    while num1 != 0:
        current_dig = num1 % 10

        if current_dig % 2 == 0:
            num2 += current_dig * (10 ** num2_dig_pos)
            num2_dig_pos += 1

        num1 //= 10

    print(num2)


def q6v1():
    num1 = int(input('Enter the 1st number: '))
    num2 = int(input('Enter the 2nd number (must be of equal digits to the 1st number: '))

    res = 0
    dig_pos = 0

    while num1 >= 10 ** dig_pos:

        res *= 10
        dig_pos += 1

        temp1, temp2 = num1, num2
        while temp1 >= 10 ** dig_pos:
            temp1 //= 10
            temp2 //= 10
        temp1 %= 10
        temp2 %= 10

        res += temp1
        res *= 10
        res += temp2

    print(res)

def q6():
    num1 = int(input('Enter the 1st number: '))
    num2 = int(input('Enter the 2nd number (must be of equal digits to the 1st number: '))

    res = 0
    dig_pos = 0

    while num1 != 0 and num2 != 0:
        num1_dig, num2_dig = num1 % 10, num2 % 10

        res += num2_dig * 10 ** dig_pos
        res += num1_dig * 10 ** (dig_pos + 1)
        dig_pos += 2

        num1 //= 10
        num2 //= 10

    if num1 != 0 or num2 != 0:
        print('Invalid Input')
    else:
        print(res)


def q7():
    num = int(input('Enter a number: '))

    max_dig = 0
    while num != 0:
        current_dig = num % 10
        max_dig = current_dig if current_dig > max_dig else max_dig
        num //= 10

    print(max_dig)


def q8():
    pass


def q9():
    import random

    bingo = random.randint(1,100)
    user_guess = int(input('Guess a number from 1-100: '))
    guess_count = 1

    while user_guess != bingo:
        if user_guess < 1 or user_guess > 100:
            print('Invalid Input, try again: ', end = '')
            guess_count -= 1
        elif user_guess < bingo:
            print('Too small, try again: ', end = '')
        else:
            print('Too big, try again: ', end = '')

        user_guess = int(input())
        guess_count += 1

    print(f'\nBingo! number of guesses taken: {guess_count}')


def main():
    q1v1()
    # q1()
    # q2()
    # q3()
    # q4()
    # q5()
    # q6()
    # q7()
    # q8()
    # q9()



main()
