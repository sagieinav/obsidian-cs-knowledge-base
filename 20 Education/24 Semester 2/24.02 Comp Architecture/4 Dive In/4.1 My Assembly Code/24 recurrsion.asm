.data
	promptMessage: .asciiz "Enter a number to find its factorial: "
	resultMessage: .ascii "The factorial of the number is "
	inputNumber: .word 0
	resultNumber: .word 0
.text
	.globl main
	main:
		# Read the number from the user:
		li $v0, 4
		la $a0, promptMessage
		syscall
		
		li $v0, 5
		syscall
		
		sw $v0, inputNumber
		
		# Call the factorial function: