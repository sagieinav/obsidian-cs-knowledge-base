################# Data segment #####################
.data
str: .asciiz "Traveling to Cuba!"
str1: .space 100
msg1: .asciiz "Modified string is: "
msg2: .asciiz "The reduced string is: "

################# Code segment #########################
.text
.globl main

main:
#print the string before the change
li $v0,4
la $a0,str
syscall

#new line
li $v0,11
li $a0,'\n'
syscall

#answer:

li $t0, 0         # string index
la $t1, str  	  # address of str in memory
la $t2, str1 	  # address of str1 in memory 
li $t3, 0    	  # index for new string: str1
li $t5, '$'       # storing ASCII value of '$'

outer_loop: 
lbu $t3, 0($t1)   # load chars from string
beqz $t3, end     # check if end of string str.

sb $t3, 0($t2) 
sb $t5, 0($t1)
addi $t2, $t2, 1  # increment to next index at str1
addi $t1, $t1, 2  # increment to next 2 indexes at str
j outer_loop


end:
li $v0,4
la $a0,msg1
syscall

li $v0,4
la $a0,str
syscall

li $v0,11
li $a0,'\n'
syscall

li $v0,4
la $a0,msg2
syscall

li $v0,4
la $a0,str1
syscall

li $v0,10
syscall