.data
	message: .asciiz "After while loop is done."
	newSpace: .asciiz ", "
.text
	main:
		# Set i = 0:
		addi $t0, $zero, 0
		
		while:
			jal printNumber # Perform the operation
		
			addi $t0, $t0, 1 # i++
			
			ble $t0, 10, while # Loop condition
		exit:
			jal printEnd
		
		# End of program
		li $v0, 10
		syscall
		
	printNumber:
		li $v0, 1
		add $a0, $t0, $zero
		syscall
		
		li $v0, 4
		la $a0, newSpace
		syscall
		
		jr $ra
	
	printEnd:
		li $v0, 4
		la $a0, message
		syscall
		
		jr $ra