.data
	prompt: .asciiz "Enter your age: "
	message: .asciiz "\nYour age is "
.text
	# Prompt the user to enter age.
	li $v0, 4
	la $a0, prompt
	syscall
	
	# Get the user's age.
	li $v0, 5 # 5 is get int input operation
	syscall
	
	# Store the age in t0
	move $t0, $v0
	
	# Display the message
	li $v0, 4
	la $a0, message
	syscall
	
	# Complete the message (print the age).
	li $v0, 1
	move $a0, $t0
	syscall