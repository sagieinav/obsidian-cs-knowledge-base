.data
	number1: .word 5
	number2: .word 10

.text
# Store the values into the registers:
	lw $t0, number1($zero)
	lw $t1, number2($zero)
	
# Perform the add operation:
	add $t2, $t0, $t1 # $t2 = $t0 + $t1
	
# Print the added result:
	li, $v0, 1
	add $a0, $zero, $t2
	syscall