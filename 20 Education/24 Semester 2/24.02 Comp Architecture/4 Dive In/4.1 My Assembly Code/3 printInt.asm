.data 
	age: .word 25 # An integer is always 32bits (4bytes), so we declare a word

.text
	# Print the integer inside 'age' to the screen
	li $v0, 1
	lw $a0, age
	syscall