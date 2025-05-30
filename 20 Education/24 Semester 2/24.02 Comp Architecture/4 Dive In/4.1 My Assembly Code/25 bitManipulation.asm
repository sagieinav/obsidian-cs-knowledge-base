.data
	newLine: .asciiz "\n"
	
.text
	main:
		li $a1, 11
		jal showNumber
		
		li $a1, 11
		jal clearLsb
		
		move $a1, $v0
		jal showNumber
	
	
	
		# End the program:
		li $v0, 10
		syscall
		
	showNumber: # Expects a number in $a1
		li $v0, 4
		la $a0, newLine
		syscall
		
		li $v0, 1
		move $a0, $a1
		syscall
		
		jr $ra
	
	clearLsb:
	# Mask is $s0
	addi $sp, $sp, -4 # Yo stack, point 1 byte backwards
	sw $s0, 0($sp) # Store the mask in the address we reserved
	
	# Make the mask
	li $s0, -1
	li $s0, -1
	sll $s0, $s0, 1
	
	# Clear the LSB of the input number
	and $v0, $a1, $s0
	
	lw $s0, 0($sp)
	addi $sp, $sp 4
	
	jr $ra