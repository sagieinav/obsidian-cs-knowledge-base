import random
import string

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


def create_random_str_2d_arr():
    arr = create_empty_2d_arr()
    for row in range(len(arr)):
        for column in range(len(arr[row])):
            arr[row][column] = ''.join(random.choices(string.ascii_letters, k=1))

    return arr

def create_specific_str_2d_arr():
    arr = create_empty_2d_arr()
    for row in range(len(arr)):
        for column in range(len(arr[row])):
            arr[row][column] = ''.join(random.choices(string.ascii_letters, k=1))

    return arr


def view_as_matrix(two_d_arr):
    matrix = ''

    for row in range(len(two_d_arr)):
        for column in range(len(two_d_arr[row])):
            # matrix += str(two_d_arr[row][column]).rjust(3)
            matrix += f'{str(two_d_arr[row][column]).rjust(2)} '
        matrix += '\n'

    return matrix


def find_col_with_max_appearances(letters, ch):
    votes = [0] * len(letters[0])

    for row in range(len(letters)):
        for column in range(len(letters[row])):
            if letters[row][column] == ch:
                votes[column] += 1

    if max(votes) == 0:
        return -1

    popular_col = 0
    for col in range(1, len(votes)):
        if votes[col] > votes[popular_col] and votes[col] > 0:
            popular_col = col

    return popular_col


def max_on_edge(numbers):
    max_value = numbers[0][0]

    for row in range(len(numbers)):
        for column in range(0, len(numbers[row]), +(len(numbers[row]) -1)):
            max_value = numbers[row][column] if numbers[row][column] > max_value else max_value

    return max_value


def create_snake(rows, cols):
    arr = [[None] * cols for i in range(rows)]
    value = 1
    col_index = -1

    for times in range (len(arr)):
        for row in range (len(arr)):
            if col_index % 2 != 0:
                arr[row * -1 - 1][col_index] = value
            else:
                arr[row][col_index] = value
            value += 1
        col_index -= 1
        if abs(col_index) > cols:
            break

    return arr


def has_path(matrix):
    row = 0
    col = -1

    while True:
        
        if matrix[row][col] == "|":
            if row == len(matrix) - 1:
                return True
            else:
                row += 1

        elif matrix[row][col] == "-" and col != -(len(matrix[0])):
                col -= 1

        else:
            return False



if __name__ == '__main__':
    choice = -1
    while choice != 0:
        print('\nWhat would you like to do? \
        \n1: Create an empty 2D array \
        \n2: Enter random values into an empty 2D array \
        \n3: View a given 2D array as a matrix \
        \n4: Create a random characters 2D array \
        \n5: Check in which column a given character appears the most \
        \n6: Get the maximum value of a matrix\'s border \
        \n7: Create a Snake Matrix \
        \n8: Check if a matrix has a path \
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
            print(f'\nCreating a random characters 2D array')

            arr = create_random_str_2d_arr()
            matrix = view_as_matrix(arr)

            print(matrix)

        elif choice == 5:
            print(f'\nChecking in which column a given character appears the most')

            arr = create_random_str_2d_arr()
            matrix = view_as_matrix(arr)
            print(matrix)
            ch = input('Enter the character you want to check: ')

            column_index = find_col_with_max_appearances(arr,ch)

            print(column_index)

        elif choice == 6:
            print(f'\nGetting the maximum value of a matrix\'s border')

            arr = create_random_2d_arr()
            matrix = view_as_matrix(arr)
            print(matrix)

            max_edge_value = max_on_edge(arr)

            print(max_edge_value)

        elif choice == 7:
            print(f'\nCreating a Snake Matrix')

            rows = int(input('How many rows do you want? '))
            columns = int(input('How many columns do you want? '))

            snake_list = create_snake(rows,columns)
            print(snake_list)

            snake_matrix = view_as_matrix(snake_list)
            print(snake_matrix)

        elif choice == 8:
            print(f'\nChecking if matrix has a path')

            success1 = [['a','a','a','a','a','|']
                ,['a','a','a','a','a','|']
                ,['a','a','a','|','-','-']
                ,['a','a','|','-','a','a']
                ,['a','a','|','a','a','a']]

            success2 = [['a', 'a', 'a', 'a', 'a', '|']
                , ['a', 'a', 'a', 'a', 'a', '|']
                , ['a', 'a', 'a', '|', '-', '-']
                , ['a', 'a', '|', '-', 'a', 'a']
                , ['a', '|', '-', 'a', 'a', 'a']]

            success3 = [['a', 'a', 'a', 'a', 'a', '|']
                , ['a', 'a', 'a', 'a', 'a', '|']
                , ['a', 'a', 'a', '|', '-', '-']
                , ['a', 'a', '|', '-', 'a', 'a']
                , ['|', '-', '-', 'a', 'a', 'a']]

            fail1 = [['a', 'a', 'a', 'a', 'a', '|']
                , ['a', 'a', 'a', 'a', 'a', '|']
                , ['a', 'a', 'a', '|', '-', '-']
                , ['a', 'a', '|', '-', 'a', 'a']
                , ['a', 'a', '-', 'a', 'a', 'a']]

            fail2 = [['a', 'a', 'a', 'a', 'a', '|']
                , ['a', 'a', 'a', 'a', 'a', '|']
                , ['a', 'a', 'a', '|', '-', '|']
                , ['a', 'a', '|', '-', 'a', 'a']
                , ['a', 'a', '|', 'a', 'a', 'a']]

            fail3 = [['a', 'a', 'a', 'a', 'a', '|']
                , ['a', 'a', 'a', 'a', 'a', '|']
                , ['a', 'a', 'a', '|', '-', '-']
                , ['a', 'a', '|', '-', 'a', 'a']
                , ['-', '-', '-', 'a', 'a', 'a']]

            fail4 = [['a', 'a', 'a', 'a', 'a', '|']
                , ['a', 'a', 'a', 'a', 'a', '|']
                , ['a', 'a', 'a', '|', '-', '-']
                , ['a', 'a', '|', '-', 'a', 'a']
                , ['a', '|', 'a', 'a', 'a', 'a']]


            print(has_path(success1))
            print(has_path(success2))
            print(has_path(success3))
            print(has_path(fail1))
            print(has_path(fail2))
            print(has_path(fail3))
            print(has_path(fail4))


        elif choice == 0:
            print('Goodbye!')
            exit()

        else:
            print('Invalid Input. Please try again.')
            choice = int(input('\nEnter your choice: '))

        break
