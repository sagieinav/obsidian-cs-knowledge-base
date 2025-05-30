.data
	message: .asciiz "The number is smaller."
	
.text
	main:
		addi $t0, $zero, 199
		addi $t1, $zero, 200
	
		slt $s0, $t0, $t1
	
		bne $s0, $zero, printMessage
	
		# End the program
		li $v0, 10
		syscall
		
	printMessage:
		li $v0, 4
		la $a0, message
		syscall
	