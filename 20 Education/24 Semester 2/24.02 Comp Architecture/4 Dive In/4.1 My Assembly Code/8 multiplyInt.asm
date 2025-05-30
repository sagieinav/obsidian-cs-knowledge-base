.data
	

.text
	li $v0, 1
# 3 Different methods to perform multiplication


# First (mul) is max 16bits for each variable.
	addi $s0, $zero, 10 # s0 = 10
	addi $s1, $zero, 4 # s1 = 4
	
	mul $t0, $s0, $s1 # t0 = s0 * s1 = 10 * 4

	add $a0, $zero, $t0
	syscall
	
	
# Second (mult) supports larger numbers.
	addi $s0, $zero, 2000
	addi $s1, $zero, 10
	
	mult $s0, $s1 # Bigger numbers, they're stored in 2 registers
	mflo $t0 # Moving the product result to s2
	
	add $a0, $zero, $t0
	syscall
	

# Third (sll) using shift. Multiplies in exponents of 2. Very Efficient.
	addi $s0, $zero, 4
	
	sll $t0, $s0, 2 # t3 = s0 * 2^2 = 16
	
	add $a0, $zero, $t0
	syscall
	