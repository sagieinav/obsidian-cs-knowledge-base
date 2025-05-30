import random

def create_empty_2d_arr():
    rows = int(input('How many rows do you want? '))
    columns = int(input('How many columns do you want? '))

    empty_arr = [[None] * columns for i in range(rows)]

    return empty_arr


def rng_into_2d_arr(two_d_arr):
    for row in range(len(two_d_arr)):
        for column in range(len(two_d_arr[row])):
            two_d_arr[row][column] = random.randint(1, 99)


def create_random_2d_arr():
    arr = create_empty_2d_arr()
    for row in range(len(arr)):
        for column in range(len(arr[row])):
            arr[row][column] = random.randint(1, 99)

    return arr


def view_as_matrix(two_d_arr):
    matrix = ''

    for row in range(len(two_d_arr)):
        for column in range(len(two_d_arr[row])):
            # matrix += str(two_d_arr[row][column]).rjust(3)
            matrix += f'{str(two_d_arr[row][column]).rjust(2)} '
        matrix += '\n'

    return matrix


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
        \n1: Create an empty 2D array \
        \n2: Enter random values into an empty 2D array \
        \n3: View a given 2D array as a matrix \
        \n4: ... \
        \n5: ... \
        \n6: ... \
        \n0: Exit')
        choice = int(input('\nEnter your choice: '))

        if choice == 1:
            print(f'\nCreating an empty 2D array')

            empty_2d_arr = create_empty_2d_arr()

            print(empty_2d_arr)


        elif choice == 2:
            print(f'Entering random values into an empty 2D array...')

            two_d_arr = create_empty_2d_arr()
            rng_into_2d_arr(two_d_arr)

            print(two_d_arr)


        elif choice == 3:
            print(f'\nViewing a given 2D array as a matrix')

            arr = create_random_2d_arr()
            matrix = view_as_matrix(arr)

            print(matrix)


        elif choice == 4:
            print(f'\n...')
            func4()

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
