from operator import index


def is_switched_number(number):
	if number < 10:
		return True
	
	dig0 = number % 10
	dig1 = number // 10 % 10
	
	if (dig0 % 2 == 0 and dig1 % 2 == 0) or (dig0 % 2 != 0 and dig1 % 2 != 0):
		return False
		
	return is_switched_number(number // 10)


def has_switched_couple(number):
	if number < 10:
		return False
	
	dig0 = number % 10
	dig1 = number // 10 % 10
	
	if (dig0 % 2 == 0 and dig1 % 2 != 0) or (dig0 % 2 != 0 and dig1 % 2 == 0):
		return True
	
	return has_switched_couple(number // 10)


def switch_values(the_list, index_begin, index_end):
	if index_end == index_begin or index_end + 1 == index_begin:
		return the_list
	
	the_list[index_end], the_list[index_begin] = the_list[index_begin], the_list[index_end]
	
	return switch_values(the_list, index_begin + 1, index_end - 1)


def has_sequence_v1(the_list, num, streak = 0): # 3rd var
	if the_list[0] == streak + 1:
		streak += 1
		if streak == num:
			return True
	else:
		streak = 0
		
	if len(the_list) == 1:
		return False
	
	return has_sequence(the_list[1:], num, streak)


def has_sequence_v2(the_list, num): # 2 Functions
	def has_sequence_inside(the_list, num, streak = 0):
		if the_list[0] == streak + 1:
			streak += 1
			if streak == num:
				return True
		else:
			streak = 0
		
		if len(the_list) == 1:
			return False
		
		return has_sequence_inside(the_list[1:], num, streak)
	res = has_sequence_inside(the_list, num)
	return res


def has_sequence(the_list, num):  # With for loop
	if the_list[0] == 1:
		for i in range(1, num + 1):
			if the_list[i] != i + 1:
				break
			elif the_list[i] == num:
				return True
	
	if len(the_list) == 1:
		return False
	
	return has_sequence(the_list[1:], num)



def func5():
	pass


def func6():
	pass


if __name__ == '__main__':
	choice = -1
	while choice != 0:
		print('\nWhat would you like to do? \
        \n1: Check if a number is a switched number \
        \n2: Check if a number has a switched couple \
        \n3: Switch values of a list \
        \n4: Check if a list has a sequence of a specific digit \
        \n5: ... \
        \n6: ... \
        \n0: Exit')
		choice = int(input('\nEnter your choice: '))
		
		if choice == 1:
			print(f'\nChecking if a number is a switched number')
			
			num = int(input('Enter the number you wanna check: '))
			
			print(is_switched_number(num))
		
		elif choice == 2:
			print(f'\nChecking if a number has a switched couple')
			
			num = int(input('Enter the number you wanna check: '))
			
			print(has_switched_couple(num))
		
		elif choice == 3:
			print(f'\nSwitching values of a list')
			
			list = [10, 20, 30, 40, 50]
			index_start = 1
			index_end = 3
			
			print(switch_values(list, index_start, index_end))
		
		elif choice == 4:
			print(f'\nChecking if a list has a sequence of a specific digit')
			
			list = [3, 2, 1, 2, 3, 4, 4, 5]
			dig = 5
			
			print(has_sequence(list, dig))
		
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
