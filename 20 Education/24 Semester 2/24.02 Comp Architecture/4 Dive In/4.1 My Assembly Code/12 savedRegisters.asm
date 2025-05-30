.data
	newLine: .asciiz "\n"
.text
	main:
	# Initialization
		add $s0, $zero, 10
	
	# Print the increased value
		jal printIncreasedRegister
	
	# Print a new line	
		li $v0, 4
		la $a0, newLine
		syscall
	
	# Print the original saved value
		li $v0, 1
		move $a0, $s0
		syscall
	
# This line is going to end the program
	li $v0, 10
	syscall
	
	printIncreasedRegister:
	# First we need to save the old s0 value to the stack (by convention)
		addi $sp, $sp, -4 # Yo Stack? point to previous byte
		sw $s0, 0($sp) # Save s0's value to the first position in stack pointer
		
		addi $s0, $s0, 30 # Perform the increase
		
	# Print new value in function
		li $v0, 1
		move $a0, $s0
		syscall
		
		lw $s0, 0($sp) # Restore s0 to the original value we saved
		
		addi $sp, $sp, 4 # Yo Stack? point back to original address
		
		jr $ra # Jump back to original position (back to main)