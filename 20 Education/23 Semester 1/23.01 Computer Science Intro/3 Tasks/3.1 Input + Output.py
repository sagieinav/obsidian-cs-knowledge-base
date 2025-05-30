def rectangle():
    height = float(input('Enter the height of the triangle: '))
    width = float(input('Enter the width of the triangle: '))

    area = width * height
    
    print(f'The area is {area}')


def circle():
    PI = 3.14
    
    radius = float(input('Enter the radius of the circle: '))

    area = radius * radius * PI
    perimeter = radius * 2 * PI

    print(f'Area is {area} and perimeter is {perimeter}')


def toast():
    BASE_TOAST_PRICE = 12.0
    CHEAP_TOPPING_PRICE = 2.0
    EXP_TOPPING_PRICE = 3.0

    cheap_topping_amount = int(input('How many cheap toppings do you wanna add to your toast? '))
    exp_topping_amount = int(input('How many expensive toppings do you wanna add to your toast? '))

    to_pay = BASE_TOAST_PRICE + (CHEAP_TOPPING_PRICE*cheap_topping_amount) + (EXP_TOPPING_PRICE*exp_topping_amount)
    
    print(f'Please pay {to_pay} ILS')


def delievery():
    RATE_PER_KM = 5.0
    RATE_PER_FLOOR = 1.0
    TIP_RATE = 1.1

    item_price = float(input('What is the price of the furniture? '))
    item_weight = float(input('What is the weight of the furniture? '))
    distance_to_customer = float(input('How many kilometers for the transportation? '))
    customer_floor = int(input('How many floors? '))

    delievery_price = (RATE_PER_KM*distance_to_customer) + (RATE_PER_FLOOR*customer_floor*item_weight)
    final_price = (item_price*TIP_RATE) + delievery_price

    print(f'Please pay {final_price} ILS')



def main():
    rectangle()
    # circle()
    # toast()
    # delievery()


main()
