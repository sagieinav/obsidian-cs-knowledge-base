# Input: 1)a string (max 30 chars)in buf
#
#
# Output: 1)The number of ASCII digit from 0-9
# 2)The sum of the square of all the digits 0-9
#
##
# Example
# Please enter a string(max 30 chars)
# cabc123as
# The number of digit 0-9 in the string is:3
# The sum of the square of all the digit is:14
# -- program is finished running --
################# Data segment #####################
.data
buf: .space 31
msg1: .asciiz "\n Please enter a string(max 30 chars)\n"
msg2: .asciiz " \n The number of digit 0-9 in the string is:"
msg3: .asciiz " \n The sum of the square of all the digit is:"
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
li $a1,31 #max chars
syscall
la $a0,msg2 # The number of digit 0-9 in the string is:
li $v0,4 # system call to print
syscall # out a string

#answer

li $t0, 0      # initializing out loop index 
la $t1, buf    # load the address of buf to t1 
li $t3, 0      # count the number of ASCII digits in the string
li $t6, 0      # sum of square

outer_loop: 
bgt $t0, 31, end
lbu $t2, 0($t1)
bgt $t2, '9', increment 
blt $t2, '0', increment

addi $t2, $t2, -48
addi $t3, $t3, 1
mul  $t2, $t2, $t2 
add  $t6, $t6, $t2 

increment:
addi $t0, $t0, 1
addi $t1, $t1, 1
j outer_loop

end:
la $a0,msg2  
li $v0,4 
syscall 

move $a0, $t3  
li $v0,1 
syscall

la $a0,msg3 
li $v0,4 
syscall 



move $a0, $t6  
li $v0,1 
syscall   

li $v0,10 
syscall      