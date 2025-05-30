import random

def random_list(length = 10):
    list = [None] * length

    for item in range(len(list)):
        list[item] = random.randint(0, 100)

    return list


def even_items():
    list = random_list(10)
    print(list)

    for item in range(len(list)):
        if list[item] % 2 == 0:
            print(list[item], end = ' ')


def divided_by3_list():
    list = [None] * 10

    for item in range(len(list)):
        list[item] = item * 3
    print(list)



def bump_even_pos():
    list = random_list(10)
    print(list)

    for item in range(len(list)):
        if item % 2 == 0:
            list[item] += 1
    print(list)


def bump_i2_deduct_i3():
    list = random_list(10)
    print(list)

    for item in range(len(list)):
        if item % 2 == 0:
            list[item] += 1
        if item % 3 == 0:
            list[item] -= 1
    print(list)

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


def is_invoice_series(list):
    differential = list[1] - list[0]

    for item in range(1, len(list)):
        if list[item] - list[item - 1] != differential:
            return f'\nThe series {list} is NOT an invoice series'

    return f'\nThe series {list} is an invoice series'


def common_values(list1, list2):
    # new_list = [None] * max(len(list1), len(list2))
    new_list = []

    for l1_index in range(len(list1)):
        l1_item = list1[l1_index]

        for l2_index in range(len(list2)):
            l2_item = list2[l2_index]
            if l1_item == l2_item:
                new_list.append(l2_item)

    return new_list if new_list else 'There are no common values'


def min_values_index(list):
    min = list[0]
    indexes_list = [0]

    for i in range(1, len(list)):
        if list[i] < min:
            min = list[i]
            indexes_list = [i]
        elif list[i] == min:
            indexes_list.append(i)

    return indexes_list


def is_reverse_list(list1, list2):
    for i in range(len(list1)):
        if list1[i] != list2[-(i + 1)]:
            return f'{list1} does NOT equal {list2} reversed'

    return f'{list1} EQUALS {list2} reversed'


def is_ascending_list(list):
    for i in range(1, len(list)):
        if list[i] <= list[i-1]:
            return f'{list} is NOT an ascending-order list.'

    return f'{list} is an ascending-order list.'


def diagram_graph(list):
    max_val = max(list)

    for row in range(max_val, 0, -1):
        for i in range(len(list)):
            if list[i] >= row:
                print('*', end = ' ')
            else:
                print(' ', end = ' ')
        print()

    #Cosmetic:
    for i in range(len(list)):
        print('-', end = ' ')
    print()
    for i in range(len(list)):
        print(list[i], end = ' ')
    print()


def sum_lists (list1, list2):
    longer_l, shorter_l = (list1, list2) if len(list1) >= len(list2) else (list2, list1)
    summed_list = [None] * (len(longer_l) + 1)
    leftover = 0

    for i in range(len(longer_l)):
        item = longer_l[-i -1] + leftover
        if i < (len(shorter_l)):
            item += shorter_l[-i -1]

        if item > 9:
            item -= 10
            leftover = 1
        else:
            leftover = 0

        summed_list[-i -1] = item

    if leftover == 1:
        summed_list[0] = 1
    else:
        summed_list.remove(None)

    return summed_list



if __name__ == '__main__':
    choice = -1
    while choice != 0:
        print('\nWhat would you like to do? \n1: Check if a list is an invoice series\
         \n2: Find the common values of 2 given lists\
         \n3: Find the indexes of a list\'s minimum values\
          \n4: Check for 2 given lists if they are equal but reversed\
           \n5: Check if a given list is an ascending list\
            \n6: Create a diagram-graph from a list\
              \n7: Sum 2 lists into 1 list\
             \n0: Exit')
        choice = int(input('\nEnter your choice: '))
        print()

        if choice == 1:
            print(f'\nChecking if a list is an invoice series.')

            is_invoice = is_invoice_series((input_list()))

            print(is_invoice)


        elif choice == 2:
            print(f'\nCreating a list with the common values of 2 given lists.')

            list1 = random_list()
            list2 = random_list(8)

            res_list = common_values(list1, list2)

            print(f'The common values of {list1} and {list2} are:\n{res_list}')


        elif choice == 3:
            print(f'\nFinding the indexes of a list\'s minimum values.')

            list = random_list(20)

            min_indexes_list = min_values_index(list)

            print(f'The items with the minimum values in {list} are in index/es: {min_indexes_list}')

        elif choice == 4:
            print('Checking for 2 lists if they are equal but reversed')

            list1 = input_list()
            list2 = input_list()

            print(is_reverse_list(list1, list2))

        elif choice == 5:
            print('Checking if a list is an ascending list')

            list = input_list()

            print(is_ascending_list(list))

        elif choice == 6:
            print('Creating a diagram-graph from a random list.')

            list = random_list(6, 9)

            print(f'Diagram graph of the list {list}:\n')
            diagram_graph(list)

        elif choice == 7:
            print('Summing 2 lists into 1 list')

            list1 = [9, 9, 9, 9]
            list2 = [9, 7]
            sum = sum_lists_v1(list1, list2)

            print(f'List1: {list1} \nList2: {list2} \nSum = {sum}')

        elif choice == 0:
            print('Goodbye!')
            exit()

        else:
            print('Invalid Input. Please try again.')
            choice = int(input('\nEnter your choice: '))

        break
