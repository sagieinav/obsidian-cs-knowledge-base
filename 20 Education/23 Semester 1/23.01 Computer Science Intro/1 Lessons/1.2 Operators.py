def q1():
    num = int(input('Enter a 4-digit number: '))

    left = num // 100
    right = num % 100

    result = (left % 10 + left // 10) / 2 == (right % 10 + right // 10)
    
    print('Does the number meet the requirement?', result)


def q2():
    num = int(input('Enter a 4-digit number: '))
    
    first_dig = num // 1000
    second_dig = num // 100 % 10
    third_dig = num % 100 // 10
    fourth_dig = num % 10

    is_divided_by3 = (num % 3 == 0)
    is_palindrom = (first_dig == fourth_dig and second_dig == third_dig)
    result = is_palindrom and is_divided_by3

    print('Does the number meet the requirement?', result)


def q3():
    MIN_CLASSES = 80
    MIN_TASKS = 70

    classes_percent = float(input('What percentage of the total classes amount have you participated in? '))
    tasks_percent = float(input('What percentage of the total tasks have you completed? '))
    is_task5 = input('Have you completed task #5? (y/n) ')

    result = (is_task5 == 'y' and classes_percent >= MIN_CLASSES and tasks_percent >= MIN_TASKS)

    print(f'Can the student participate in the final exam? {result}')


def q4():
    num = int(input('Enter a 5-digit number: '))

    dig0 = num % 10
    dig1 = num % 100 // 10
    dig2 = num // 100 % 10
    dig3 = num // 1000 % 10
    dig4 = num // 10000

    avg_even = (dig0 + dig2 + dig4) / 3
    avg_odd = (dig1 + dig3) / 2
    res = avg_even == avg_odd

    print(f'Does the number {num} meet the requirement? {res}')


def q5():
    num1 = int(input('Enter a 3-digit number: '))
    num2 = int(input('Enter another 3-digit number: '))

    n1_dig0 = num1 % 10
    n1_dig1 = num1 // 10 % 10
    n1_dig2 = num1 // 100

    n2_dig0 = num2 % 10
    n2_dig1 = num2 // 10 % 10
    n2_dig2 = num2 // 100

    is_divided_by11 = (num1 * num2) % 11 == 0
    is_reversed = n1_dig0 == n2_dig2 and n1_dig1 == n2_dig1 and n1_dig2 == n2_dig0
    res = is_divided_by11 and is_reversed

    print(f'Do these numbers meet the requirement? {res}')


def main():
    q1()
    # q2()
    # q3()
    # q4()
    # q5()


main()
