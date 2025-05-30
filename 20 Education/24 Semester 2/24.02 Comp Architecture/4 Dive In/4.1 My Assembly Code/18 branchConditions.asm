.data
	messageEquals: .asciiz "The numbers are equal."
	messageNothing: .asciiz "Nothing happened."
.text
	main:
		addi $t0, $zero, 20
		addi $t1, $zero, 20
		
		beq $t0, $t1, numbersEqual
		bne $t0, $t1 numbersNotEqual
	
	# End the program
	li $v0, 10
	syscall
	
	numbersEqual:
		li $v0, 4
		la $a0, messageEquals
		syscall
		
		li $v0, 10
		syscall
	
	numbersNotEqual:
		li $v0, 4
		la $a0, messageNothing
		syscall
		
