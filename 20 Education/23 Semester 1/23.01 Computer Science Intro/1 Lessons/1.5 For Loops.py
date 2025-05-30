def q1():
    num = int(input('Enter a number: '))
    for i in range(num+1):
        print (f'{i} --> {i ** 2}')


def q2():
    odd_count = 0
    print('Enter 5 numbers: ')

    for i in range(5):
        num = int(input())
        if num % 2 != 0:
            odd_count += 1

    print(f'There are {odd_count} odd numbers')


def q3():
    num = int(input('Enter a number: '))
    print('All numbers that are times of 3: ')

    for i in range (num+1):
        if i % 3 == 0:
            print(i, end = ' ')


def q4():
    num = int(input('Enter a number: '))
    print('All numbers that up to {num} except times of 7: ')

    for i in range(1, num + 1):
        if i % 7 == 0:
            print('boom!', end=' ')
        else:
            print(i, end = ' ')


def q5():
    num = int(input('Enter a 2-digit number: '))
    if num < 10 or num > 99:
        print('Invalid Input')
        exit()

    for i in range(1, num + 1):
        dig_sum = i // 10 + i % 10
        if dig_sum == 5:
            print(i, end = ' ')


def q6():
    base = int(input('How many signs in each line? '))

    for row in range(base+1):
        for star in range(row):
            print('*', end = '')
        for hash in range(base - row):
            print('#', end = '')
        print()


def q7():
    num = int(input('Enter a number: '))

    for row in range(1, num+1):
        for l_star in range(row):
            print('*', end = '')
        for space in range((num - row) * 2):
            print(' ', end = '')
        for r_star in range(row):
            print('*', end='')
        print()


def q8():
    num = int(input('Enter a number: '))

    for carpet in range(num):
        for row in range(num):
            for sector in range(num):
                for star in range(num):
                    print('*', end = '')
                print(' ', end = '')
            print()
        print()


def main():
    # q1()
    # q2()
    # q3()
    # q4()
    # q5()
    # q6()
    # q7()
    q8()


main()
