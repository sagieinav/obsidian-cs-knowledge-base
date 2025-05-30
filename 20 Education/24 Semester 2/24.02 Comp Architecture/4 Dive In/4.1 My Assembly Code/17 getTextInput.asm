.data
	prompt: .asciiz "Please enter your name: "
	message: .asciiz "\nHello, "
	userInput: .space 20 # Reserve 20 bytes, to allow the user to enter 20 characters.
.text
	main:
		# Print prompt to the user
		li $v0, 4
		la $a0, prompt
		syscall
	
		# Get user's input (text)
		li $v0, 8
		la $a0, userInput # The address goes into $a0
		li $a1, 20 # We limit to 20 chars. Goes into $a1
		syscall
		
		# Display the initial message
		li $v0, 4
		la $a0, message
		syscall
		
		# Print the name
		la $a0, userInput
		syscall
		
	
	# Tell the system that 'main' ends here
	li $v0, 10
	syscall