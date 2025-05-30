################# Data segment #####################
.data
str: .asciiz "Traveling to Cuba!"
str1: .space 100
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

answer:
