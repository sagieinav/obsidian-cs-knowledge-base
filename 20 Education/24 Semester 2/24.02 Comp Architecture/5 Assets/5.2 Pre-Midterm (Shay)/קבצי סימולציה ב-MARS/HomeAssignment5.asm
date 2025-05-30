# home assignment 5:

.data

myStr: .space 19
msg1: .asciiz "Please enter a string"
msg2: .asciiz "The string you entered is: "

.text
main: 

#print a message to the console:
li $v0,4
la $a0,msg1
syscall

la $a0, myStr
li $a1, 18
li $v0,8
syscall

#New line:
li $v0,11
li $a0,'\n'
syscall

li $v0,4
la $a0,msg2
syscall

li $v0,4
la $a0,myStr
syscall

li $v0, 10
syscall

#New line:
li $v0,11
li $a0,'\n'
syscall

############################################
#  - - - part A 
#  inverting small <-> capital letters in array

