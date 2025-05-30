.data
	myArray: .word 100:5 # ([100, 100, 100])
	newLine: .asciiz "\n"

.text
	main: 
		# Clear index / offset to 0:
		addi $t0, $zero, 0
	
		while: # Prints the array
			# Load the current integer:
			lw $t1, myArray($t0)
		
			# Print the current integer:
			li $v0, 1
			move $a0, $t1
			syscall
		
			# Print a new line (cosmetic)
			li $v0, 4
			la $a0, newLine
			syscall
	
			addi $t0, $t0, 4 # i++
			bne $t0, 20, while # Loop condition (branch if i != 5)
	
		# End the program:
		li $v0, 10
		syscall
