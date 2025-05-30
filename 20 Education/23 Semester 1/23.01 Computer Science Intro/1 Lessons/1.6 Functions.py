def draw_isoceles_trianlge(base, distance = 0):
    for row in range(1, base + 1):
        for margin in range(distance):
            print(' ', end = '')
        for spaces in range(base - row):
            print(' ', end = '')
        for stars in range(row):
            print('* ', end = '')
        print()


def draw_opposite_isoceles_trianlge(base, distance = 0):
    for row in range(1, base + 1):
        for margin in range(distance):
            print(' ', end='')
        for spaces in range(row - 1):
            print(' ', end='')
        for stars in range(base - (row - 1)):
            print('* ', end='')
        print()


def draw_sandclock(base):
    draw_opposite_isoceles_trianlge(base)
    draw_isoceles_trianlge(base)


def draw_rectangle(width, height, distance):
    for rectangle_row in range(height):
        for space in range(distance):
            print(' ', end='')
        for star in range(width):
            print('*', end='')
        print()


def draw_christmas_tree(num_of_triangles):
    base = 3
    distance = num_of_triangles - 1

    for triangle in range(num_of_triangles):
        draw_isoceles_trianlge(base, distance)
        base += 1
        distance -= 1

    draw_rectangle(3, 5, num_of_triangles)


def q1():
    draw_isoceles_trianlge(4, 3)


def q2():
    draw_opposite_isoceles_trianlge(4, 3)


def q3():
    draw_sandclock(5)


def q4():
    draw_rectangle(3, 5, 5)


def q5():
    draw_christmas_tree(4)


def q6():
    pass


def q7():
    pass


def q8():
    pass


def main():
    # q1()
    # q2()
    # q3()
    # q4()
    q5()
    # q6()
    # q7()
    # q8()


main()