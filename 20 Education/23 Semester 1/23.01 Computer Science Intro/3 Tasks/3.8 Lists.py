import random

def input_list(length = 6):
    list = [None] * length

    print(f'Forming a list. Please enter {length} numbers: ')
    for item in range(len(list)):
        list[item] = int(input())

    return list


def random_list(length = 6, max = 100):
    list = [None] * length

    for item in range(len(list)):
        list[item] = random.randint(0, max)

    return list


def mirrored_couple(num1, num2):
    num_reversed = 0
    target = num2
    while num1 > 0:
        if num2 == 0:
            return False
        current_dig = num1 % 10
        num_reversed *= 10
        num_reversed += current_dig

        num1 //= 10
        num2 //= 10

    if num2 != 0:
        return False
    elif num_reversed == target:
        return True
    else:
        return False


def is_mirror_list(numbers):
    for i in range(0, len(numbers) // 2 + 1):
        if not mirrored_couple(numbers[i], numbers[-i-1]):
            return False
    return True


def is_kaprekar1(num):
    res_arr = []
    if num <= 1:
        return res_arr

    resha = num ** 2
    sepha = 0
    dig_pos = 0

    while resha != 0:
        current_dig = resha % 10
        sepha += current_dig * 10 ** dig_pos
        dig_pos += 1
        resha //= 10

        if resha + sepha == num and resha != 0 and sepha != 0:
            res_arr = [resha, sepha]
            return res_arr

    return res_arr



def is_kaprekar2(num):
    res_arr = []
    if num <= 1:
        return res_arr

    squared = str(num ** 2)

    for i in range(1, len(squared)):
        resha = int(squared[0:i])
        sepha = int(squared[i:len(squared)])

        if resha + sepha == num and resha != 0 and sepha != 0:
            res_arr = [resha, sepha]
            return res_arr

    return res_arr


if __name__ == '__main__':
    choice = -1
    while choice != 0:
        print('\nWhat would you like to do? \
        \n1: Check if 2 numbers are a mirrored couple \
        \n2: Check if a list is a mirrored collection \
        \n3: Check if a number is a Kaprekar number \
        \n4: ... \
        \n5: ... \
        \n6: ... \
        \n0: Exit')
        choice = int(input('\nEnter your choice: '))

        if choice == 1:
            print(f'\nChecking if 2 numbers are a mirrored couple')

            num1 = int(input('Enter the 1st number: '))
            num2 = int(input('Enter the 2nd number: '))

            print(mirrored_couple(num1,num2))

        elif choice == 2:
            print(f'\nChecking if a list is a mirrored collection')

            list = input_list(5)

            print(is_mirror_list(list))

        elif choice == 3:
            print(f'\nChecking if a number is a Kaprekar number')

            num = 100
            print(is_kaprekar1(num))

        elif choice == 4:
            print(f'\n...')


        elif choice == 5:
            print(f'\n...')


        elif choice == 6:
            print(f'\n...')


        elif choice == 0:
            print('Goodbye!')
            exit()

        else:
            print('Invalid Input. Please try again.')
            choice = int(input('\nEnter your choice: '))

        break