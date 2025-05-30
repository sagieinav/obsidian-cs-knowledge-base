# your id: 12345678

# Question 1
def count_tens_units(dig_list, num):
	return count_tens_units_helper(dig_list, num, len(dig_list))

def count_tens_units_helper(dig_list, num, length, count = 0):
	tens_dig = num // 10
	singles_dig = num % 10
	
	if length == 1:
		return count
	
	if dig_list[length - 1] == singles_dig and dig_list[length - 2] == tens_dig:
		count += 1
	
	return count_tens_units_helper(dig_list, num, length - 1, count)
	

# Question 2
def is_number_exist(matrix, row, col, num):
	if row >= len(matrix) or col >= len(matrix[0]):
		return -1
	tens_dig = num // 10
	singles_dig = num % 10
	
	if matrix[row][col] != tens_dig:
		return False
	
	# Here current index is indeed tens dig. Now searching for singles dig around it.
	start_row = max(row - 1, 0)
	end_row = min(row + 2, len(matrix))
	start_col = max(col - 1, 0)
	end_col = min(col + 2, len(matrix[0]))
	
	for i in range(start_row, end_row):
		for j in range(start_col, end_col):
			if matrix[i][j] == singles_dig and not (i == row and j == col):
				return True
	return False
	

def where_number_in_2dim_list(matrix, num):
	res = []
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if is_number_exist(matrix, i, j, num):
				res.append([i,j])
	
	return res


# Question 3
def neighbors_avg(list, n, i):
	if n % 2 == 0 or i >= len(list):
		return -1
	
	sum = 0
	start = i - n // 2
	end = i + 1 + n // 2
	if start < 0 or end > len(list):
		return list[i]
	for i in range(start, end):
		sum += list[i]
	avg = sum / n
	
	return avg


def create_avg_neighbors(list, n):
	avg_list = [x for x in list]
	for i in range(len(list)):
		avg_list[i] = neighbors_avg(list, n, i)
	
	return avg_list


#Question 4
def count_substring(st_list, st):
	count = 0
	for word in st_list:
		while st in word:
			count += 1
			word = word.replace(st[0], '', 1)
	
	return count


# main fucntion
def main():
# Question 1 tests:
	l1 = [4, 2]
	l2 = [2, 4]
	l3 = [4, 1, 2, 3, 9]
	l4 = [4, 2, 4, 2, 4]
	l5 = [4]
	num = 42
	
	print(count_tens_units(l5, num))

# Question 2 tests:
	matrix = [
		[5, 8, 3, 2, 1, 3],
		[2, 4, 3, 8, 7, 2],
		[4, 9, 7, 7, 4, 8],
		[1, 3, 8, 3, 9, 6]
	]
	num = 34
	print(is_number_exist(matrix, 3, 3, num))
	print(where_number_in_2dim_list(matrix, num))

# Question 3 tests:
	list = [-10, -1, 8, 5, 1, 3, 8, 10, 12, 3]
	n = 5
	i = 4
	print(neighbors_avg(list, n, i))
	print(create_avg_neighbors(list, n))

# Question 4 tests:
	st_list1, st1 = ['abcdbcabc'], 'bc'
	st_list2, st2 = ['abcdbcabc', 'efg', 'bc'], 'bc'
	st_list3, st3 = ['aaaa', 'abc'], 'aa'
	st_list4, st4 = ['bcc', 'ccb', 'abccba'], 'bccb'

	print(f'Check1: {count_substring(st_list1, st1)}')
	print(f'Check2: {count_substring(st_list2, st2)}')
	print(f'Check3: {count_substring(st_list3, st3)}')
	print(f'Check4: {count_substring(st_list4, st4)}')
	
	signs = '#@!$'
	number = 12304560
	
	print(tali_the_best_hostess(signs, number))


if __name__ == "__main__":
	main()