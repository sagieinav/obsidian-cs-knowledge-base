.data
	prompt: .asciiz "Enter the value of e: "
.text
	# Display the message to the user
	li $v0, 4
	la $a0, prompt
	syscall
	
	# Get the input from the user (double)
	li $v0, 7 # Input gets stored in $f0 and $f1
	syscall
	
	# Print the user's input (double)
	li $v0, 3
	add.d $f12, $f0, $f2 # all unused $f registers, like $f2 here, just store 0.0 value
	syscall