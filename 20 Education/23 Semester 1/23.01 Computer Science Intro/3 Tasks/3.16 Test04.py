from unittest.util import unorderable_list_difference


def check_seq_len_c(list, i, j): # Part A
	# CHECK LEFT STREAK
	l_streak = 1
	# Check starting elements:
	element = list[i][j]
	next_element = list[i][j - l_streak]
	# Check all coming elements:
	while element + 1 == next_element and l_streak < len(list[i]): # While left streak is ongoing
		l_streak += 1
		element = next_element
		next_element = list[i][j - l_streak]
	
	# CHECK DOWN STREAK
	d_streak = 1
	# Check starting elements:
	element = list[i][j]
	while i + d_streak == len(list) or len(list[i + d_streak]) <= j: # Find next compatible row
		if i + d_streak == len(list): # If next row is out of range, jump back to first row
			i = - d_streak
		else: # Else, jump to next row
			i += 1
	next_element = list[i + d_streak][j]
	# Check all coming elements:
	while element + 1 == next_element and d_streak < len(list): # While down streak is ongoing
		d_streak += 1
		element = next_element
		while len(list[i + d_streak]) <= j: # Find next compatible row
			if i + d_streak == len(list): # If next row is out of range, jump back to first row
				i =  - d_streak
			else: # Else, jump to next row
				i += 1
		next_element = list[i + d_streak][j]
	
	return max(d_streak, l_streak)


def check_all_seq_c(list): # Part B
	res = []
	for i in range(len(list)):
		for j in range(len(list[i])):
			if check_seq_len_c(list, i, j) >= 3:
				res.append([check_seq_len_c(list, i, j), i, j])
	
	return res
	
	

def func3():
	pass


def func4():
	pass


def func5():
	pass


def func6():
	pass


if __name__ == '__main__':
	list = [
		[1,24,26,2],
		[2,14,27,38,35,5],
		[67,66,65,70,69,68],
		[91,2,92],
		[73,7,51,71,9,62],
		[85,4,64,72,10],
		[24,47,25,1,45,14],
		[42,41]
		]
	
	print(check_seq_len_c(list, 6, 2))
	
	print(check_all_seq_c(list))