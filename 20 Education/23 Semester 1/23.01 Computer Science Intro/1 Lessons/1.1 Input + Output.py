def q1():
    fav_city = input('What is your favorite city? ')
    country = input('What country is this city located in? ')
    print(fav_city + ',', country)

def q2():
    STARTING_TARIF = 10.20
    KM_TARIF = 1.30
    SUITCASE_TARIF = 2.0  # Float because we may want to change the tarif to something else

    suitcase_quantity = int(input('How many suitcases do you have? '))
    ride_distance = float(input('What is the distance to your destination in kilometers? '))

    final_price = STARTING_TARIF + ride_distance * KM_TARIF + suitcase_quantity * SUITCASE_TARIF

    print(f'The price for your requested ride is {final_price}₪')


def q3():
    STOP_DELAY = 5.0
    TRAVEL_TIME_PER_FLOOR = 3.0

    elevator_floor = int(input('What floor is the elevator in right now? '))
    user_floor = int(input('What floor are you in right now? '))
    destination_floor = int(input('What is your destination floor? '))

    to_user = (abs(user_floor - elevator_floor)) * TRAVEL_TIME_PER_FLOOR
    to_destination = (abs(user_floor - destination_floor)) * TRAVEL_TIME_PER_FLOOR
    total_time = to_user + STOP_DELAY + to_destination

    print(f'\nTotal time of your travel is {total_time} seconds')


def main():
    # q1()
    # q2()
    q3()

main()
