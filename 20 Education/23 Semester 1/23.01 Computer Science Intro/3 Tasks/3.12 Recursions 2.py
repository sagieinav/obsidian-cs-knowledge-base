def like_fibo(nth):
	if nth <= 3:
		return nth
	
	elif nth % 2 == 0:
		return like_fibo(nth - 1) + like_fibo(nth - 2) + like_fibo(nth - 3)
	else:
		return abs(like_fibo(nth - 1) - like_fibo(nth - 3))


def count_letter(words, ch):
	length = len(words)
	return helper_counter(words, ch, length)


def helper_counter(words, ch, length, count = 0):
	if length == 0:
		return count
	
	for letter in words[length - 1]:
		if letter == ch:
			count += 1
	return helper_counter(words, ch, length -1, count)


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
        \n1: Like Fibo \
        \n2: Count letters \
        \n3: ... \
        \n4: ... \
        \n5: ... \
        \n6: ... \
        \n0: Exit')
		choice = int(input('\nEnter your choice: '))
		
		if choice == 1:
			print(f'\n...')
			print(like_fibo(11))
		
		elif choice == 2:
			print(f'\nCounting letters')
			print(count_letter(['gogo', 'momo', 'yoyo', 'katooooooov', 'mini', 'yofi', 'nahon nahonnnnn!!!!!'], 'o'))
		
		elif choice == 3:
			print(f'\n...')
		
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
