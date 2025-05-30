def equation():
    ax = float(input('Please enter the value of Ax: '))
    if ax == 0:
        print('No Solution')
        exit()

    b = float(input('Please enter the value of B: '))
    if b == 0:
        print('Infinite solutions')
        exit()

    solution = -b / ax
    print(solution)


def wedding():
    relationship = input('Enter relationship (family / close / other): ')

    if relationship != 'family' and relationship != 'close' and relationship != 'other':
        print('Invalid Input')
        exit()

    if relationship == 'family':
        gift = 1000

    else:
        acquaintance = float(input('Enter years of acquaintance: '))
        if acquaintance < 0:
            print('Invalid Input')
            exit()

        travel_time = float(input('Enter travel time in hours: '))
        if travel_time < 0:
            print('Invalid Input')
            exit()

        gift = 500 if relationship == 'close' else 250

        if acquaintance > 3:
            gift += 50
        if travel_time > 1:
            gift -= 50


    print(f'Recommended gift amount: {gift} NIS')


def library():
    GENERAL_MAX = 5 # (= ADULT MAXIMUM)
    CHILD_MAX = 3

    is_expired = input('Does this subscription have a book that is leased for more than a month? (y/n) ')
    if is_expired == 'y':
        print(False)
        exit()
    elif is_expired != 'n':
        print('Invalid Input')
        exit()
    # Finished check #1 (lease > 1month)

    books_amount = int(input('How many leased books does this subscription currently have? '))
    if books_amount < 0:
        print('Invalid Input')
        exit()
    if books_amount >= GENERAL_MAX:
        print(False)
        exit()
    if books_amount < CHILD_MAX:
        print(True)
        exit()
    # Finished check #2 (general leased books amount)

    sub_type = input('What is the subscription type? (adult/child) ')
    if sub_type == 'adult':
        print(True)
    elif sub_type == 'child':
        print(False)
    else:
        print('Invalid Input')
    # Finished check #3 (specific leased books amount)


def lilput():
    MIN_DIPLOMA_GRADE = 102
    MIN_PSYCHO_GRADE = 700
    MIN_PSYCHO_CALC_GRADE = 145
    MIN_PSYCHO_ENG_GRADE = 120
    MIN_WEIGHTED_GRADE = 600

    diploma_grade = float(input('What is your matriculation certificate\'s average grade? '))
    if diploma_grade < 0:
        print('Invalid Input')
        exit()
    if diploma_grade >= MIN_DIPLOMA_GRADE:
        print(True)
        exit()
    # Finished check #1 (diploma avg grade)

    psycho_grade = int(input('What is your psychometric exam grade? '))
    if psycho_grade < 200 or psycho_grade > 800:
        print('Invalid Input')
        exit()
    weighted_grade = psycho_grade * 0.8 + diploma_grade / 1.2
    if weighted_grade >= MIN_WEIGHTED_GRADE:
        print(True)
        exit()
    # Finished check #2 (weighted grade)

    if psycho_grade < MIN_PSYCHO_GRADE:
        print(False)
        exit()
    # Finished check #3.1 (psycho general grade)

    psycho_calc_grade = int(input('What is your psychometric exam\'s calculation part grade? '))
    if psycho_calc_grade < 50 or psycho_calc_grade > 150:
        print('Invalid Input')
        exit()
    if psycho_calc_grade < MIN_PSYCHO_CALC_GRADE:
        print(False)
        exit()
    # Finished check #3.2 (psycho calc grade)

    psycho_eng_grade = int(input('What is your psychometric exam\'s English part grade? '))
    if psycho_eng_grade < 50 or psycho_eng_grade > 150:
        print('Invalid Input')
        exit()
    if psycho_eng_grade >= MIN_PSYCHO_ENG_GRADE:
        print(True)
    else:
        print(False)
    # Finished check #3.3 (psycho ENG grade) and all of check #3


def training_plan():
    heart_beat = int(input('What is your resting heart-beat? '))

    if heart_beat > 70:
        km_amount = 3

    else:
        experience = int(input('What is your training experience in weeks? '))

        if experience < 1:
            print('Invalid Input')
            exit()

        if experience < 3:
            km_amount = 3
        elif experience < 5:
            km_amount = 5
        elif heart_beat < 60:
            km_amount = 10
        else:
            km_amount = 8

    print(km_amount)


def grade_calc():
    exam_grade = int(input('What is your exam grade? (0-100) '))
    if exam_grade < 0 or exam_grade > 100:
        print('Invalid Input')
        exit()

    tasks_avg = float(input('What is your tasks\'s average grade? (0-100) '))
    if tasks_avg < 0 or tasks_avg > 100:
        print('Invalid Input')
        exit()

    q_tasks_completed = int(input('How many tasks have you completed? (0-8) '))
    if q_tasks_completed < 0 or q_tasks_completed > 8:
        print('Invalid Input')
        exit()


    if q_tasks_completed <= 4:
        final_grade = 0

    elif q_tasks_completed <= 6:
        if (exam_grade >= 55):
            final_grade = 0.8 * exam_grade + 0.2 * tasks_avg
        else:
            final_grade = exam_grade

    elif tasks_avg > exam_grade: # (7-8 tasks completed and MAGEN is improving)
        if (exam_grade >= 55):
            final_grade = 0.7 * exam_grade + 0.3 * tasks_avg
        elif (tasks_avg >= 80):
            final_grade = 0.75 * exam_grade + 0.25 * tasks_avg
        else:
            final_grade = 0.8 * exam_grade + 0.2 * tasks_avg

    else: # (7-8 tasks completed but MAGEN is NOT improving)
        final_grade = exam_grade

    print(final_grade)


def main():
    # equation()
    # wedding()
    # library()
    lilput()
    # training_plan()
    # grade_calc()


main()
