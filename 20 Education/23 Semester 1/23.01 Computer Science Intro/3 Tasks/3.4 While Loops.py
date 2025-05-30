def q1():
    num = int(input('Enter a positive number: '))
    if num < 0:
        print('Invalid Input')
        exit()

    dig = int(input('Enter a digit: '))
    if dig < 0 or dig > 9:
        print('Invalid Input')
        exit()

    if dig == 0 and num == 0:
        print(1)
        exit()

    dig_presence = 0

    while num != 0:
        current_dig = num % 10
        if current_dig == dig:
            dig_presence += 1
        num //= 10

    print(dig_presence)


def q2():
    num = int(input('Enter a positive number: '))
    if num < 0:
        print('Invalid Input')
        exit()

    new_num = 0
    dig_pos = 0

    while num != 0:
        current_dig = num % 10
        new_num += current_dig * 10 ** dig_pos

        dig_pos += 1
        num //= 100

    print(new_num)


def q3():
    num1 = int(input('Enter a positive number: '))
    if num1 < 0:
        print('Invalid Input')
        exit()
    num2 = int(input('Enter another positive number, (must be of equal digits to your 1st number): '))
    if num2 < 0:
        print('Invalid Input')
        exit()

    equiv_digs = 0

    while num1 != 0 and num2 != 0:
        num1_dig = num1 % 10
        num2_dig = num2 % 10
        if num1_dig == num2_dig:
            equiv_digs += 1
        num1 //= 10
        num2 //= 10

    if num1 != 0 or num2 != 0:
        print('Invalid Input - your numbers are not of equal digits amount')
    else:
        print(equiv_digs)


def q4():
    id = int(input('Please enter your ID number, including check digit: '))

    if id < 10 ** 7 or id >= 10 ** 9 : # ID is <8 digits or >9 digits
        print('Invalid Input. ID must be of 8-9 digits length.')
        exit()

    check_digit = id % 10
    raw_id = id // 10

    dig_sum = 0
    is_even_dig = True

    while raw_id != 0:
        current_dig = raw_id % 10 * 2 if is_even_dig else raw_id % 10
        current_dig = current_dig % 10 + current_dig // 10

        dig_sum += current_dig
        raw_id //= 10
        is_even_dig = not is_even_dig

    is_valid_id = (dig_sum + check_digit) % 10 == 0

    print(is_valid_id)


def q5():
    num = int(input('Enter a positive number: '))
    if num < 0:
        print('Invalid Input')
        exit()

    new_num = 0
    dig_pos = 0

    while num >= 10:
        current_pair = num % 100
        new_pair = (current_pair % 10 * 10) + current_pair // 10
        new_num += new_pair * 10 ** dig_pos

        dig_pos += 2
        num //= 100

    if num != 0:
        new_num += num * 10 ** dig_pos

    print(new_num)


def q6():
    num = int(input('Enter a positive number: '))
    if num < 0:
        print('Invalid Input')
        exit()

    rev_num = 0
    num_length = 0

    temp = num
    while temp != 0:
        num_length += 1
        rev_num *= 10
        rev_num += temp % 10
        temp //= 10

    res = num * 10 ** num_length + rev_num
    print(res)


def q7v1():
    while True:
        expression = input('Enter a math expression representing a sum of 2 numbers (i.e \'4+6\'): ')

        is_plus = expression.find('+') > 0 and expression.find('+') < len(expression) - 1 \
                  and expression.count('+') == 1
        if not is_plus:
            is_minus = expression.find('-') > 0 and expression.find('-') < len(expression) - 1 \
                       and expression.count('-') == 1
            if not is_minus:
                print('Invalid Input')
            exit()

        expr_list = expression.split('+')

        num1 = int(expr_list[0])
        num2 = int(expr_list[1])
        subtraction = abs(num1 - num2)  # Destined to be left dig/s
        addition = num1 + num2 # Destined to be right dig/s

        temp = addition
        dig_count = 0
        while temp != 0:
            dig_count += 1
            temp //= 10
        new_num = subtraction * 10 ** dig_count + addition

        print(new_num)

def q7():
    operator = 0
    while operator != '-':
        num1 = int(input('Enter 2 positive numbers with the \'+\' operator. To stop, enter \'-\'. \nEnter the 1st number: '))
        if num1 < 0:
            print('Invalid Input')
            exit()

        operator = input('Enter the operator (\'+\' to use the algorithm, \'-\' to stop): ')
        if operator != '+' and operator != '-':
            print('Invalid Input')
            exit()

        num2 = int(input('Enter the 2nd number: '))
        if num2 < 0:
            print('Invalid Input')
            exit()

        subtraction = abs(num1 - num2)  # Destined to be left dig/s
        addition = num1 + num2  # Destined to be right dig/s

        temp = addition
        dig_count = 0
        while temp != 0:
            dig_count += 1
            temp //= 10
        new_num = subtraction * 10 ** dig_count + addition

        print(new_num)


def main():
    # q1()
    # q2()
    # q3()
    q4()
    # q5()
    # q6()
    # q7()


main()