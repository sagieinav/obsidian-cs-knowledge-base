.data 
	array: .word 10, 2, 9
	arrLength: .word 3
	sum: .word 0
	average: .word 0
.text
	main:
		la $t0, array # Base arr address
		li $t1, 0 # i = 0
		lw $t2, arrLength
		li $t3, 0 # sum = 0
		
		sumLoop:
			lw $t4, ($t0) # $t4 = array[i] 
			add $t3, $t3, $t4 # Sum up
			
			add $t1, $t1, 1 # i++
			add $t0, $t0, 4 # Update the array address	
			
			blt $t1, $t2, sumLoop # loop while i < length
			
		sw $t3, sum
			
		# Calculate the average:
		div $t5, $t3, $t2 # $t5 = sum / length
		sw $t5, average
		
		# Display sum.
		li $v0, 1
		move $a0, $t3
		syscall
		
		# Display average
		li $v0, 1
		move $a0, $t5
		syscall
			
		# End the program
		li $v0, 10
		syscall