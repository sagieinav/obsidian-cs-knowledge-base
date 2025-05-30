.data
# In assembly, a function is called a procedure.
	message: .asciiz "Hi everybody.\nMy name is Sagi.\n"	
	
.text
	main:
	# Call the function to print the string
		jal displayMessage
		
	# Print number 5 to the screen	
		addi $s0, $zero, 5
	
		li $v0, 1
		add $a0, $zero, $s0
		syscall
	
	
	# End the program, to prevent infinite loop:	
		li $v0, 10
		syscall
	
	displayMessage:
		li $v0, 4
		la $a0, message
		syscall
		
		jr $ra # Go back to the precedure that called this procedure