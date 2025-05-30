def q1():
    count = 0 # Only for validating results

    for denominator in range(11, 100):
        eins_deno = denominator % 10

        if eins_deno != 0:
            for numerator in range(10, denominator):
                eins_nume = numerator // 10

                if numerator / denominator == eins_nume / eins_deno:
                    print(f'{eins_nume}/{eins_deno} == {numerator}/{denominator}')
                    count += 1 # Only for validating results

    print(count) # Only for validating results


def q2():
    num1 = int(input('Enter a positive number: '))
    num2 = int(input('Enter another positive number with digits amount equal to your previous number: '))

    new_num = 0
    new_dig_pos = 0
    new_dig_power = 10 ** new_dig_pos

    while num1 != 0 and new_num < 10 ** 8: # Running on all right digits of num1 and num2
        num1_dig0 = num1 % 10
        num2_dig0 = num2 % 10
        for i in range(num1_dig0):
            if new_num < 10 ** 8:
                new_num += num2_dig0 * new_dig_power
                new_dig_pos += 1
                new_dig_power = 10 ** new_dig_pos

        num1 //= 10
        num2 //= 10

    print(new_num)

def q3():
    num = int(input('Enter a positive number: '))
    user_dig = int(input('Enter a digit: '))

    new_num = 0
    dig_pos = 0

    while num != 0:
        section = 0
        for i in range(user_dig):
            current_dig = num % 10
            section *= 10
            section += current_dig

            num //= 10
            if num == 0:
                break

        new_num += section * 10 ** dig_pos
        dig_pos += user_dig

    print(new_num)


def q4():
    base = int(input('How many signs in each line? '))

    for row in range(1,base + 1):
        for star in range(row):
            print('*', end='')
        for hash in range(base - row):
            print('#', end='')
        print()


def q5():
    base = int(input('What is the base of the triangle? '))

    for row in range(base):
        for space in range(row):
            print(' ', end = '')
        for star in range(base - row):
            print('*', end = ' ')
        print()


def q6():
    base = int(input('What is the base of the triangle? (odd number) '))

    for row in range(base):
        for space in range(row):
            print(' ', end='')
        for star in range(base - row):
            print('*', end=' ')
        print()

    for row in range(1, base + 1):
        for space in range(base - row):
            print(' ', end='')
        for star in range(row):
            print('*', end=' ')
        print()


def q7():
    num = int(input('Enter a number: '))

    for carpet in range(num):
        for row in range(num):
            for sector in range(num):
                for star in range(num):
                    print('*', end='')
                print(' ', end='')
            print()
        print()


def q8():
    base = int(input('What is the base of the triangle? (odd number) '))

    for triangle in range(3):
        for row in range(1, base + 1):
            for space in range(base - row):
                print(' ', end='')
            for star in range(row):
                print('*', end=' ')
            print()
    for trunk in range(base):
        for space in range(base - 1):
            print(' ', end = '')
        print('*')


def q9():
    TARGET = 10

    mates_count = 0
    num = 1

    while mates_count < TARGET:
        dividers_sum = 0

        for divider in range(num // 2, 0, -1):
            if num % divider == 0:
                dividers_sum += divider

        if dividers_sum > num:
            candidate = dividers_sum
            cand_dividers_sum = 0
            for divider in range(candidate // 2, 0, -1):
                if candidate % divider == 0:
                    cand_dividers_sum += divider
            if cand_dividers_sum == num:
                mates_count += 1
                print(f'{mates_count}) {num} and {candidate} are mates')

        num += 1


def q10():
    num = 10
    streak = 0
    happy_count = 0

    while streak < 3:
        temp = num
        while temp >= 10:
            dig_sum = 0
            while temp != 0:
                dig = temp % 10
                dig_sum += dig ** 2
                temp //= 10
            temp = dig_sum

        if dig_sum == 1:
            streak += 1
            happy_count += 1
            print(f'{happy_count}) {num} is a happy number :-)')
        else:
            streak = 0

        num += 1

    print(num - 3, num - 2, num - 1)


def main():
    # q1()
    # q2()
    # q3()
    # q4()
    # q5()
    # q6()
    # q7()
    # q8()
    q9()
    # q10()

main()
