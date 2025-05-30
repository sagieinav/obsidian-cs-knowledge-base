#Question1:(80%)
# Input: 1)a string (max 40 chars)in buf
# 2)a char (ASCII)
#
# Output: 1)The string is copied to buf1 replace the char with '*'
# if there are more than five replacements the char to replace with is '@'
# 2)print the new string
#
## Example:
#
#Please enter a string(max 40 chars)
# aaabbbaaabbbaaabbb
# Please enter a char:b
# The string with the char replaced is:
# aaa***aaa**@aaa@@@
################# Data segment #####################
.data
buf: .space 41
buf1: .space 41
msg1: .asciiz "\n Please enter a string(max 40 chars)\n"
msg2: .asciiz " \n Please enter a char:"
msg3: .asciiz " \n The string with the char replaced is:\n"
################# Code segment #####################
.text
.globl main
main: # main program entry
la $a0,msg1 # Please enter a string(max 40 chars)
li $v0,4 # system call to print
syscall # out a string
# get string from the user syscall 8
li $v0,8
la $a0,buf #the start address of the string
li $a1,41 #max chars
syscall
la $a0,msg2 # Please enter a char
li $v0,4 # system call to print
syscall # out a string
li $v0,12
syscall

#answer

move $t0, $v0 

li $t1, 0 # index for outer loop
li $t2, 0 # count the number of occurences 
la $t3, buf  # address in memory of buf 
la $t4, buf1 # address in memory of buf1

outer_for_loop: 
bgt $t1, 40, end 
addi $t1, $t1, 1
lbu $t5, 0($t3) 

check_char: 
beq $t5, $t0, replace
sb $t5, 0($t4)

increment:
addi $t3, $t3, 1 
addi $t4, $t4, 1 
j  outer_for_loop 
  
replace:
bgt $t2, 4, replace2
li $t5, '*' 
addi $t2, $t2, 1
sb $t5, 0($t4) 
j  increment
 
replace2:
li $t5, '@' 
sb $t5, 0($t4) 
j  increment

end: 
# Print buf1 string: 
la $a0, msg3
li $v0, 4
syscall 

la $a0, buf1
li $v0, 4
syscall

li $v0, 10
syscall 
