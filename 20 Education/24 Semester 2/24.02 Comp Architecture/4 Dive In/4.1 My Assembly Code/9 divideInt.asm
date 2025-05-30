.data

.text
	li $v0, 1
	addi $t0, $zero, 30
	addi $t1, $zero, 7
	
# Option 1 (rs, rt, rd):
	div $s0, $t0, $t1
	
	move $a0, $s0
	syscall
	
# Option 2 (rs, rd, immediate):
	div $s0, $t0, 10
	
	move $a0, $s0
	syscall

# Option 3 (store in lo & hi):
	div $t0, $t1 # lo = t0 / t1, hi = t0 % t1
	mflo $s0 # s0 = t0 / t1
	mfhi $s1 # s1 = t0 % t1
	
	move $a0, $s0
	syscall
	move $a0, $s1
	syscall