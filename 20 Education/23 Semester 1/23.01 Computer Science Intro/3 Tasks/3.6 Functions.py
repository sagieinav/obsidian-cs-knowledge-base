def get_dividers_sum(num):
    dividers_sum = 0

    for divider in range(num // 2, 0, -1):
        if num % divider == 0:
            dividers_sum += divider

    return dividers_sum


def are_friends(num1, num2):
    if get_dividers_sum(num1) == num2:
        return True
    return False


def create_successive_number(num):
    bumped_num = 0
    dig_pos = 0

    while num != 0:
        current_dig = num % 10
        if current_dig == 9:
            current_dig = 0
        else:
            current_dig += 1

        bumped_num += current_dig * 10 ** dig_pos
        dig_pos += 1

        num //= 10

    return bumped_num


def draw_rhombus(size, ch):
    for row in range(1, size + 1):
        for sign1 in range(size - (row - 1)):
            print(ch, end = '')
        for space in range((row - 1) * 2):
            print(' ', end = '')
        for sign2 in range(size - (row - 1)):
            print(ch, end='')
        print()

    for row in range(1, size):
        for sign1 in range(row + 1):
            print(ch, end='')
        for space in range((size - row - 1) * 2):
            print(' ', end='')
        for sign2 in range(row + 1):
            print(ch, end='')
        print()


def new_number_from_min_digits(num1, num2):
    res = 0
    dig_pos = 0

    while num1 != 0:
        if num2 == 0:
            return -1

        num1_dig = num1 % 10
        num2_dig = num2 % 10
        if num1_dig < num2_dig:
            min_dig = num1_dig
        else:
            min_dig = num2_dig

        res += min_dig * 10 ** dig_pos
        dig_pos += 1

        num1 //= 10
        num2 //= 10

    if num2 != 0:
        return -1
    return res

def func2():
    pass


def func3():
    pass


def func4():
    pass


def func5():
    pass


def func6():
    pass


if __name__ == '__main__':
    choice = -1
    while choice != 0:
        print('\nWhat would you like to do? \
        \n1: Check if 2 numbers are mates \
        \n2: Create a successive number \
        \n3: Draw a rhombus \
        \n4: Create a new number from min digits of 2 numbers \
        \n5: ... \
        \n6: ... \
        \n0: Exit')
        choice = int(input('\nEnter your choice: '))

        if choice == 1:
            print(f'\nChecking if 2 numbers are mates')

            num1 = int(input('Enter the 1st number: '))
            num2 = int(input('Enter the 2nd number: '))

            print(are_friends(num1, num2))

        elif choice == 2:
            print(f'\nCreating a successive number')

            num = int(input('Enter your number: '))

            print(create_successive_number(num))

        elif choice == 3:
            print(f'\nDrawing a rhombus')

            num = int(input('Enter a number: '))
            sign = input('Enter a sign: ')

            draw_rhombus(num, sign)


        elif choice == 4:
            print(f'\nCreating a new number from min digits of 2 numbers')

            num1 = int(input('Enter the 1st number: '))
            num2 = int(input('Enter the 2nd number: '))

            print(new_number_from_min_digits(num1, num2))


        elif choice == 5:
            print(f'\n...')
            func5()

        elif choice == 6:
            print(f'\n...')
            func6()

        elif choice == 0:
            print('Goodbye!')
            exit()

        else:
            print('Invalid Input. Please try again.')
            choice = int(input('\nEnter your choice: '))

        break