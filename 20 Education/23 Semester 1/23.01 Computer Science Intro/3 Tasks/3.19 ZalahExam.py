def number_of_instances(number_list, num):
	return helper_number_of_instances(number_list, num, len(number_list) - 1,0)

def helper_number_of_instances(number_list, num, size, count):
	if size == 0:
		return count

	if num == number_list[size]:
		return helper_number_of_instances(number_list, num , size - 1, count =+ 1)
	
	return helper_number_of_instances(number_list, num, size - 1, count)


def get_sum_bounded_segment(the_lists, start_row, start_col, end_row, end_col):
	counter = 0

	for i in range(len(the_lists)):
		for j in range(len(the_lists[i])):
			if start_row <= i <= end_row and start_col <= j <= end_col:
				counter += the_lists[i][j]
				
	return counter

def sum_all_bounded_segments(the_lists):
	counter = 0
	for i in range(len(the_lists)):
		for j in range(len(the_lists[i])):
			if the_lists[i][j] == 0:
				start_row = i ,j = start_col
			if the_lists[i][j] == 0:
				end_row = i, j= end_col

			return get_sum_bounded_segment (the_lists, start_row, start_col, end_row, end_col)

	return counter


def most_expensive_resturant(resturants, dishes):
	new_dict = {}

	for resturant in resturants:
		name = resturant["name"]
		new_dict[name] = 0
		
		for menu in resturant["menu"]:
			for price in dishes:
				if price["dish_id"] == menu:
					new_dict[name] += price["price"]

	max_price = max(new_dict.values())
	the_resturant = {resturant for resturant, price in new_dict.items() if price == max_price}

	return the_resturant

def how_many_dishes_from_category(resturants, dishes, category):
	new_dict = {}

	for name in resturants:
		name = name["name"]

	for typo in dishes:
		if category == typo["category"]:
			for id in resturants:
				if typo["dish_id"] == id["menu"]:
					new_dict["name"] += 1

	return new_dict



def main():
	number_list = [2,7,4,2,8,9,2,3,1]
	list2 = []
	# num = 2
	# print(number_of_instances(number_list, num))
	# print(number_of_instances(list2, num))
	#number_list2 = []
	#num2 =2
	#print(number_of_instances(number_list2, num2))
	#
	# mat = [[1, 2, 0],
	# 	   [3, 0, 3, 5, 2],
	# 		[1, 3, 0, 0]
	# 		]
	#
	# print(get_sum_bounded_segment(mat, 0, 1, 1, 2))
	#
	# print(sum_all_bounded_segments(mat))
	
	dishes = [
		dict(dish_id=101, name="Caesar Salad", category="starter", price=45),
		dict(dish_id=102, name="Beef Burger", category="main", price=75),
		dict(dish_id=103, name="Tiramisu", category="dessert", price=35),
		dict(dish_id=104, name="Vanilla Ice Cream", category="dessert", price=27)
	]
	
	resturants = [
		{"name": "Downtown Kitchen", "city": "Tel Aviv", "menu": [101, 102, 104]},
		{"name": "Port Restaurant", "city": "Haifa", "menu": [102, 103]},
		{"name": "Beach Bistro", "city": "Herzliya", "menu": [101, 102, 103, 104]}
	]
	
	print(most_expensive_resturant(resturants, dishes))

if __name__ == "__main__":
	main()