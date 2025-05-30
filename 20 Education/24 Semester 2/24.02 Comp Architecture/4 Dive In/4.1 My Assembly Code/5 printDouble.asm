.data
	myDouble: .double 7.202
	zeroDouble: .double 0.0 # We declare a zero double for future-use
	
.text
	# IMPORTANT: When storing double in registers, we only use EVEN registers
	ldc1 $f2, myDouble # Load-double into co-processor 1, registers $f2 and $f3 (we need 2 registers to hold a double)
	ldc1 $f0, zeroDouble # Will be stored in $f0 and $f1
	
	li $v0, 3
	add.d $f12, $f2, $f0 # Add myDouble and zeroDouble into $f12
	syscall # 7.202 will be printed