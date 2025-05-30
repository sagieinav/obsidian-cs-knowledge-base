# ---------------------------------------------------- #
.data
array:   .word -4,300,-600,-750,1270,-200,800,900
array1:  .space 32   # allocate space for 8 words 
msg1:    .asciiz "The given array is: "
msg2:    .asciiz "The positive even numbers of array1 are: "
spacing: .asciiz "  "

# ---------------------------------------------------- #
.text

main: 
la $a0, msg1
li $v0, 4
syscall 

# ----------------------------------------------
# for loop that will be given in the quiz itself
# The loop prints the given array:
li $t0, 0       # loop index
li $t6, 7       # array size
la $t1, array   # array address

init_loop: 
bgt $t0, $t6, continue
lw $t2, 0($t1)

move $a0, $t2 
li $v0, 1
syscall 

la $a0, spacing 
li $v0, 4
syscall  
 
addi $t0, $t0, 1
addi $t1, $t1, 4
j init_loop

# ----------------------------------------------
continue:
la $a0, '\n'
li $v0, 11
syscall

la $a0, msg2
li $v0, 4
syscall  

la $t0, array
la $t1, array1
li $t6, 0           # index for outer loop 
 
outer_loop:
bgt $t6, 7, end
lw $t2, 0($t0)      # load numer from array
mul $t2, $t2, -1    # change sign of the given number

# check is the number is divisible by 4:
andi $t3, $t2, 3
beqz $t3, storeDividedValue
sw $t2, 0($t1)      # store in array1
j check_for_print

storeDividedValue:
sra $t2, $t2, 2     # divide the number by 4
sw $t2, 0($t1)      # store in array1

check_for_print:
andi $t3, $t2, 1
bnez $t3, increment
blt $t2, 0, increment
move $a0, $t2       # print the number to console
li $v0, 1 
syscall 

la $a0, spacing     # print a space
li $v0, 4 
syscall 

increment:
addi $t0, $t0, 4
addi $t1, $t1, 4
addi $t6, $t6, 1
j outer_loop

end:
# exit the program:  
li $v0, 10 
syscall   