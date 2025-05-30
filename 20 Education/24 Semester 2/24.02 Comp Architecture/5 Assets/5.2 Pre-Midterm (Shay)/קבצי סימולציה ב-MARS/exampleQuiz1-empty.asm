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
