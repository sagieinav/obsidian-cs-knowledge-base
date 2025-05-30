def func1():
    pass


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
        \n1: ... \
        \n2: ... \
        \n3: ... \
        \n4: ... \
        \n5: ... \
        \n6: ... \
        \n0: Exit')
        choice = int(input('\nEnter your choice: '))

        if choice == 1:
            print(f'\n...')
            func1()

        elif choice == 2:
            print(f'\n...')
            func2()

        elif choice == 3:
            print(f'\n...')
            func3()

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