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
		jal printTheValue
	
# This line is going to end the program
	li $v0, 10
	syscall
	
	printIncreasedRegister:
	# First we need to save the old s0 value to the stack (by convention)
		addi $sp, $sp, -8 # Yo Stack? point 2 positions backwards
		sw $s0, 0($sp) # Save s0's value to the first position in stack pointer
		sw $ra, 4($sp) # Save the return address to second position in stack
		
		addi $s0, $s0, 30 # Perform the increase
		
	# Nested procedure:
		jal printTheValue
		
		lw $s0, 0($sp) # Restore s0 to its' original value we saved
		lw $ra, 4($sp) # Restore the original return address (main's address)
		
		addi $sp, $sp, 8 # Yo Stack? point back to original address
		
		jr $ra # Jump back to original position (back to main)
	
	printTheValue:
		li $v0, 1
		move $a0, $s0
		syscall
		
		jr $ra