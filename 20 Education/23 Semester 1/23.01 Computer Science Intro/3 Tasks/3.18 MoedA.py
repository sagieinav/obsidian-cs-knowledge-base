def reverse_text(the_text):
	return reverse_text_helper(the_text, len(the_text))


def reverse_text_helper(the_text, length, index=1):
	if len(the_text) == length * 2 - 1:  # Stop condition
		return the_text
	
	the_text = the_text[index] + ',' + the_text[0:index] + the_text[index + 1:]
	index += 2
	
	return reverse_text_helper(the_text, length, index)


def main():
	# Question 1 Tests
	st1 = 'koala'
	st2 = 'Koalas are great!'
	# st3 = ' TeStinGG,, this! complex... TEST! '
	# st4 = 'TeStinGG this! complex... TEST!'
	
	print(reverse_text(st1))
	print(reverse_text(st2))
	# print(reverse_text(st4))


if __name__ == "__main__":
	main()