.data
	PI: .float 3.14 # We declare a float

.text
	li $v0, 2
	lwc1 $f12, PI # Load-word into co-processor 1
	syscall