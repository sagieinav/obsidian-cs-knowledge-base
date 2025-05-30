.data
	myArray: .space 12 # (Allocate 3 words)
	newLine: .asciiz "\n"

.text
	main: 
		addi $s0, $zero, 4
		addi $s1, $zero, 10
		addi $s2, $zero, 12
	
		# Index / Offset = $t0
		addi $t0, $zero, 0
	
		# Store integers in the array:
		sw $s0, myArray($t0)
			addi $t0, $t0, 4 # i++
		sw $s1, myArray($t0)
			addi $t0, $t0, 4 # i++
		sw $s2, myArray($t0)
			addi $t0, $t0, 4 # i++
		
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
			bne $t0, 12, while # Loop condition
	
		# End the program:
		li $v0, 10
		syscall
