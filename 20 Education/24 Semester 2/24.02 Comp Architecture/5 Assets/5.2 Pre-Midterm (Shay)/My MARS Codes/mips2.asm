.data
# Code in this section will be written to the 'data' semgent, starting at PC = 0x10010000

LABEL1: .asciiz "Here is your code:"
LABEL2: .word 2, 3, 4, 5, 6, 7			# Each of these is a word
LABEL3: .space 3 				# Each space is 1 empty Byte, so we declared 3 empty Bytes here.
LABEL4: .byte 2, 3, -3, 'A', '5', 6, 0x12

.text
# Code in this section will be written to the 'text' semgent, starting at PC = 0x00400000

main:
	li $t0, 4		# Load Immediate: $t0 = 4
	li $t1, 5 		# Load Immediate: $t0 = 5

	add $t2, $t0, $t1 	# $t2 = $t0 + $t1

	la $t3, LABEL2		# Load Address: $t3 = Adr(LABEL2)
	lw $t0, 0($t3)		# Load Word: $t0 = Mem(LABEL2)

	add $t2, $t0, $t1	# $t2 = $t0 + $t1

	sw $t2, 0($t3)		# Store word (sw): Mem{*LABEL2} = $t2

	li $v0, 10		# Terminate program by placing $v0 = 10

	syscall



