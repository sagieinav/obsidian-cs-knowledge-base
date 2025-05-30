.data
	prompt: .asciiz "Enter the value of PI: "
	zeroAsFloat: .float 0.0
.text
	lwc1 $f4, zeroAsFloat
	
	# Display the prompt
	li $v0, 4
	la $a0, prompt
	syscall
	
	# Read user's input (float)
	li $v0, 6 # Stores the input in $f0
	syscall
	
	# Print the value (float)
	la $v0, 2
	add.s $f12, $f0, $f4 # f12 is the register that gets printed when printing float
	syscall