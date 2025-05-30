# Computer Organization & Assembly - Task no. 4 (Procedures)
# Name: Sagi Einav


.data
array: .byte 18, -2, 13, -4, 120, -6, 7, -8, -50, 12

prompt_base: .asciiz "In what base to print 2-10? "
space: .asciiz " "
newline: .asciiz "\n"
minus_sign: .asciiz "-"


.text
.globl main

main:
    # --- Read and validate base ---
read_base_loop:
    # Print prompt
    li $v0, 4          # syscall code for print string
    la $a0, prompt_base
    syscall

    # Read integer
    li $v0, 5          # syscall code for read integer
    syscall
    move $t0, $v0      # Store input in t0

    # Validate input (2 <= t0 <= 10)
    blt $t0, 2, invalid_base
    bgt $t0, 10, invalid_base

    # Valid input, store in $a1 and exit loop
    move $a1, $t0
    j end_read_base_loop

invalid_base:
    j read_base_loop

end_read_base_loop:
    # --- Call procedures ---

    # Print newline before first array print for clean output
    li $v0, 4          # syscall code for print string
    la $a0, newline
    syscall

    # Print array signed (סעיף ב)
    la $a0, array      # Pass array address to $a0
    # $a1 already contains the base (from input)
    jal print_array_sign
    li $v0, 4          # syscall code for print string
    la $a0, newline    # Print newline after array print
    syscall

    # Print array unsigned (סעיף ג)
    la $a0, array      # Pass array address
    # $a1 already contains the base
    jal print_array_unsign
    li $v0, 4
    la $a0, newline
    syscall

    # Calculate and print sum signed (סעיף ד)
    la $a0, array      # Pass array address
    # $a1 already contains the base
    jal sum_sign
    li $v0, 4
    la $a0, newline
    syscall

    # Calculate and print sum unsigned (סעיף ה)
    la $a0, array      # Pass array address
    # $a1 already contains the base
    jal sum_unsign
    li $v0, 4
    la $a0, newline
    syscall

    # Print differences signed (סעיף ו)
    la $a0, array      # Pass array address
    # $a1 already contains the base
    jal print_dif_sign
    li $v0, 4
    la $a0, newline
    syscall

    # Print sums unsigned (סעיף ז)
    la $a0, array      # Pass array address
    # $a1 already contains the base
    jal print_sum_unsign
    li $v0, 4
    la $a0, newline
    syscall


    # --- Exit program ---
    li $v0, 10         # syscall code for exit
    syscall


# ===================================================================
# Procedures
# ===================================================================

# -------------------------------------------------------------------
# Procedure: print_base (סעיף א)
# Description: Prints a 32-bit signed integer ($a2) in the specified base ($a1, 2-10).
# Handles negative numbers by printing '-' then absolute value.
# Uses stack to store digits for printing in reverse order.
# Arguments:
#   $a1 - Base (2-10)
#   $a2 - Signed 32-bit number to print
# Uses: $t0 (number), $t1 (base), $t2 (remainder/digit), $t5 (stack base pointer)
# Stack: Allocates 40 bytes for digits.
# -------------------------------------------------------------------
print_base:
    # Stack frame setup: Allocate space for digits
    # Max 32 digits for 32-bit number in base 2. Allocate 40 bytes for safety and word alignment.
    addi $sp, $sp, -40
    move $t5, $sp # Store base of digit stack ($sp before pushing digits)

    # Handle negative numbers: Check if $a2 is negative (32-bit signed)
    bltz $a2, handle_negative_pb

    # Number is non-negative, proceed with conversion
    move $t0, $a2 # Copy number to $t0
    move $t1, $a1 # Copy base to $t1
    j convert_loop_pb

handle_negative_pb:
    # Print minus sign
    li $v0, 4          # syscall code for print string
    la $a0, minus_sign
    syscall
    # Negate number to get absolute value
    sub $t0, $zero, $a2 # Calculate absolute value into $t0
    move $t1, $a1       # Copy base to $t1
    j convert_loop_pb

convert_loop_pb:
    # Loop condition: Check if number ($t0) is zero
    # Special case: If the original number was 0, we need to print '0'.
    # This check handles the initial 0 case and the loop termination.
    beq $t0, $zero, print_digits_pb_check_zero

    # Divide number by base (use unsigned division as we operate on positive/absolute value)
    divu $t0, $t1 # Divide number ($t0) by base ($t1)
    mfhi $t2     # Remainder (digit) goes to $t2
    mflo $t0     # Quotient (new number) goes to $t0

    # Push remainder (digit) onto the stack (store as byte)
    addi $sp, $sp, -1 # Move stack pointer down by 1 byte
    sb $t2, 0($sp)    # Store digit byte at the new $sp

    # Loop
    j convert_loop_pb

print_digits_pb_check_zero:
    # After convert_loop_pb finishes ($t0 is 0).
    # If stack pointer is still at $t5, it means no digits were pushed (original number was 0).
    beq $sp, $t5, print_zero_pb # If stack empty after conversion, must have been 0

print_digits_loop_pb:
    # Loop condition: While stack pointer is not back at the initial base position ($t5)
    beq $sp, $t5, end_print_base # If stack is empty, done printing digits

    # Pop digit byte
    lbu $t2, 0($sp)   # Load digit byte (unsigned load)
    addi $sp, $sp, 1  # Move stack pointer up by 1 byte (pop)

    # Convert digit value to ASCII character
    addi $a0, $t2, '0' # Add '0' ASCII value to the digit

    # Print character
    li $v0, 11         # syscall code for print character
    syscall

    # Loop
    j print_digits_loop_pb

print_zero_pb:
    # Only reached if the original number was 0
    li $a0, '0'        # ASCII value for '0'
    li $v0, 11         # syscall code for print character
    syscall
    j end_print_base   # Done printing

end_print_base:
    # Restore stack pointer (deallocate stack frame)
    addi $sp, $sp, 40 # Add back the allocated space

    # Return
    jr $ra             # Return to caller

# -------------------------------------------------------------------
# Procedure: print_array_sign (סעיף ב)
# Description: Prints a 10-element byte array as signed integers in the specified base.
# Arguments:
#   $a0 - Address of the array
#   $a1 - Base (2-10)
# Uses: $s0 (loop counter i), $s1 (base), $s2 (array pointer), $ra (saved)
# Stack: Saves $ra, $s0, $s1, $s2 (16 bytes)
# Calls: print_base, syscall (print space)
# -------------------------------------------------------------------
print_array_sign:
    # Stack frame setup: Save callee-saved registers and return address
    addi $sp, $sp, -16 # Allocate space for 4 registers
    sw $ra, 12($sp)    # Save return address
    sw $s0, 8($sp)     # Save $s0
    sw $s1, 4($sp)     # Save $s1
    sw $s2, 0($sp)     # Save $s2

    # Save arguments into callee-saved registers to use $a registers for print_base call
    move $s2, $a0 # Array address from $a0 to $s2 (s2 holds the base address of the array)
    move $s1, $a1 # Base from $a1 to $s1
    li $s0, 0     # Loop counter i = 0

print_array_sign_loop:
    # Loop condition: i < 10 (array_size)
    bge $s0, 10, end_print_array_sign_loop # If i >= 10, end loop

    # Calculate address of array[i]
    add $t0, $s2, $s0 # address = base_address ($s2) + i ($s0) * byte_size (1)

    # Load array element (signed byte)
    lb $t1, 0($t0) # Load byte at calculated address $t0 into $t1 (sign extended)

    # Pass the sign-extended value to $a2 for print_base
    move $a2, $t1

    # Pass base to $a1 (already saved in $s1)
    move $a1, $s1

    # Call print_base
    jal print_base

    # Print space separator (after each number)
    li $v0, 4          # syscall code for print string
    la $a0, space
    syscall

    # Increment loop counter
    addi $s0, $s0, 1 # Increment loop counter i

    # Loop
    j print_array_sign_loop

end_print_array_sign_loop:
    # Restore registers
    lw $ra, 12($sp)    # Restore return address
    lw $s0, 8($sp)     # Restore $s0
    lw $s1, 4($sp)     # Restore $s1
    lw $s2, 0($sp)     # Restore $s2
    addi $sp, $sp, 16  # Restore stack pointer

    # Return
    jr $ra

# -------------------------------------------------------------------
# Procedure: print_array_unsign (סעיף ג)
# Description: Prints a 10-element byte array as unsigned integers in the specified base.
# Arguments:
#   $a0 - Address of the array
#   $a1 - Base (2-10)
# Uses: $s0 (loop counter i), $s1 (base), $s2 (array pointer), $ra (saved)
# Stack: Saves $ra, $s0, $s1, $s2 (16 bytes)
# Calls: print_base, syscall (print space)
# -------------------------------------------------------------------
print_array_unsign:
    # Stack frame setup: Save callee-saved registers and return address
    addi $sp, $sp, -16 # Allocate space
    sw $ra, 12($sp)    # Save return address
    sw $s0, 8($sp)     # Save $s0
    sw $s1, 4($sp)     # Save $s1
    sw $s2, 0($sp)     # Save $s2

    # Save arguments into callee-saved registers
    move $s2, $a0 # Array address ($s2 holds the base address of the array)
    move $s1, $a1 # Base
    li $s0, 0     # Loop counter i = 0

print_array_unsign_loop:
    # Loop condition: i < 10 (array_size)
    bge $s0, 10, end_print_array_unsign_loop # If i >= 10, end loop

    # Calculate address of array[i]
    add $t0, $s2, $s0 # address = base_address ($s2) + i ($s0) * byte_size (1)

    # Load array element (unsigned byte)
    lbu $t1, 0($t0) # Load byte at calculated address $t0 into $t1 (zero extended)

    # Pass the zero-extended value to $a2 for print_base
    move $a2, $t1

    # Pass base to $a1 (already saved in $s1)
    move $a1, $s1

    # Call print_base
    jal print_base

    # Print space separator
    li $v0, 4          # syscall code for print string
    la $a0, space
    syscall

    # Increment loop counter
    addi $s0, $s0, 1         # Increment loop counter i

    # Loop
    j print_array_unsign_loop

end_print_array_unsign_loop:
    # Restore registers
    lw $ra, 12($sp)    # Restore return address
    lw $s0, 8($sp)     # Restore $s0
    lw $s1, 4($sp)     # Restore $s1
    lw $s2, 0($sp)     # Restore $s2
    addi $sp, $sp, 16  # Restore stack pointer

    # Return
    jr $ra

# -------------------------------------------------------------------
# Procedure: sum_sign (סעיף ד)
# Description: Calculates and prints the sum of signed array elements.
# Arguments:
#   $a0 - Address of the array
#   $a1 - Base (2-10)
# Uses: $s0 (loop counter i), $s1 (base), $s2 (array pointer), $s3 (sum), $ra (saved)
# Stack: Saves $ra, $s0, $s1, $s2, $s3 (20 bytes)
# Calls: print_base
# -------------------------------------------------------------------
sum_sign:
    # Stack frame setup: Save callee-saved registers and return address
    addi $sp, $sp, -20 # Allocate space for 5 registers
    sw $ra, 16($sp)    # Save return address
    sw $s0, 12($sp)    # Save $s0
    sw $s1, 8($sp)     # Save $s1
    sw $s2, 4($sp)     # Save $s2
    sw $s3, 0($sp)     # Save $s3 (for sum)

    # Save arguments into callee-saved registers
    move $s2, $a0 # Array address ($s2 holds the base address of the array)
    move $s1, $a1 # Base
    li $s0, 0     # Loop counter i = 0
    li $s3, 0     # Initialize sum to 0

sum_sign_loop:
    # Loop condition: i < 10 (array_size)
    bge $s0, 10, end_sum_sign_loop # If i >= 10, end loop

    # Calculate address of array[i]
    add $t0, $s2, $s0 # address = base_address ($s2) + i ($s0) * byte_size (1)

    # Load array element (signed byte)
    lb $t1, 0($t0) # Load byte at calculated address $t0 into $t1 (sign extended)

    # Add element to sum
    add $s3, $s3, $t1 # Add sign-extended value to sum

    # Increment loop counter
    addi $s0, $s0, 1         # Increment loop counter i

    # Loop
    j sum_sign_loop

end_sum_sign_loop:
    # Print the final sum
    move $a2, $s3 # Move sum to $a2 for print_base
    move $a1, $s1 # Move base to $a1 for print_base
    jal print_base

    # Restore registers
    lw $ra, 16($sp)    # Restore return address
    lw $s0, 12($sp)    # Restore $s0
    lw $s1, 8($sp)     # Restore $s1
    lw $s2, 4($sp)     # Restore $s2
    lw $s3, 0($sp)     # Restore $s3
    addi $sp, $sp, 20  # Restore stack pointer

    # Return
    jr $ra

# -------------------------------------------------------------------
# Procedure: sum_unsign (סעיף ה)
# Description: Calculates and prints the sum of unsigned array elements.
# Arguments:
#   $a0 - Address of the array
#   $a1 - Base (2-10)
# Uses: $s0 (loop counter i), $s1 (base), $s2 (array pointer), $s3 (sum), $ra (saved)
# Stack: Saves $ra, $s0, $s1, $s2, $s3 (20 bytes)
# Calls: print_base
# -------------------------------------------------------------------
sum_unsign:
    # Stack frame setup: Save callee-saved registers and return address
    addi $sp, $sp, -20 # Allocate space
    sw $ra, 16($sp)    # Save return address
    sw $s0, 12($sp)    # Save $s0
    sw $s1, 8($sp)     # Save $s1
    sw $s2, 4($sp)     # Save $s2
    sw $s3, 0($sp)     # Save $s3 (for sum)

    # Save arguments into callee-saved registers
    move $s2, $a0 # Array address ($s2 holds the base address of the array)
    move $s1, $a1 # Base
    li $s0, 0     # Loop counter i = 0
    li $s3, 0     # Initialize sum to 0

sum_unsign_loop:
    # Loop condition: i < 10 (array_size)
    bge $s0, 10, end_sum_unsign_loop # If i >= 10, end loop

    # Calculate address of array[i]
    add $t0, $s2, $s0 # address = base_address ($s2) + i ($s0) * byte_size (1)

    # Load array element (unsigned byte)
    lbu $t1, 0($t0) # Load byte at calculated address $t0 into $t1 (zero extended)

    # Add element to sum
    # Regular `add` works fine for adding positive values as long as the result fits in 32 bits.
    add $s3, $s3, $t1 # Add zero-extended value to sum

    # Increment loop counter
    addi $s0, $s0, 1         # Increment loop counter i

    # Loop
    j sum_unsign_loop

end_sum_unsign_loop:
    # Print the final sum (treat sum as signed for print_base)
    move $a2, $s3 # Move sum to $a2 for print_base
    move $a1, $s1 # Move base to $a1 for print_base
    jal print_base

    # Restore registers
    lw $ra, 16($sp)    # Restore return address
    lw $s0, 12($sp)    # Restore $s0
    lw $s1, 8($sp)     # Restore $s1
    lw $s2, 4($sp)     # Restore $s2
    lw $s3, 0($sp)     # Restore $s3
    addi $sp, $sp, 20  # Restore stack pointer

    # Return
    jr $ra

# -------------------------------------------------------------------
# Procedure: print_dif_sign (סעיף ו)
# Description: Calculates and prints the differences between adjacent signed array elements.
# (array[i] - array[i+1]) for i = 0 to 8.
# Arguments:
#   $a0 - Address of the array
#   $a1 - Base (2-10)
# Uses: $s0 (loop counter i), $s1 (base), $s2 (array base address), $s3 (loop limit), $ra (saved)
# Stack: Saves $ra, $s0, $s1, $s2, $s3 (20 bytes)
# Calls: print_base, syscall (print space)
# -------------------------------------------------------------------
print_dif_sign:
    # Stack frame setup: Save callee-saved registers and return address
    addi $sp, $sp, -20 # Allocate space for 5 registers
    sw $ra, 16($sp)    # Save return address
    sw $s0, 12($sp)    # Save $s0 (loop counter i)
    sw $s1, 8($sp)     # Save $s1 (base)
    sw $s2, 4($sp)     # Save $s2 (array base address)
    sw $s3, 0($sp)     # Save $s3 (loop limit)

    # Save arguments into callee-saved registers
    move $s2, $a0 # Array base address ($s2 holds the base address of the array)
    move $s1, $a1 # Base
    li $s0, 0     # Loop counter i = 0
    li $s3, 9     # Loop limit: array_size - 1 = 10 - 1 = 9 (Using $s3 - callee-saved)

print_dif_sign_loop:
    # Loop condition: i < 9
    bge $s0, $s3, end_print_dif_sign_loop # If i >= 9, end loop (Using $s3)

    # Calculate address of array[i]
    add $t1, $s2, $s0 # address of array[i] = base_address ($s2) + i ($s0) * byte_size (1)

    # Calculate address of array[i+1]
    addi $t2, $s0, 1        # calculate i+1 (in $t2)
    add $t2, $s2, $t2       # address of array[i+1] = base_address ($s2) + (i+1) ($t2)

    # Load array[i] (signed byte)
    lb $t3, 0($t1) # Load byte at calculated address $t1 into $t3 (sign extended)

    # Load array[i+1] (signed byte)
    lb $t4, 0($t2) # Load byte at calculated address $t2 into $t4 (sign extended)

    # Calculate difference: array[i] - array[i+1]
    sub $a2, $t3, $t4 # $a2 = array[i] - array[i+1]

    # Pass base to $a1 (already saved in $s1)
    move $a1, $s1

    # Call print_base
    jal print_base

    # Print space separator
    li $v0, 4          # syscall code for print string
    la $a0, space
    syscall

    # Increment loop counter
    addi $s0, $s0, 1 # Increment loop counter i

    # Loop
    j print_dif_sign_loop

end_print_dif_sign_loop:
    # Restore registers
    lw $ra, 16($sp)    # Restore return address
    lw $s0, 12($sp)    # Restore $s0
    lw $s1, 8($sp)     # Restore $s1
    lw $s2, 4($sp)     # Restore $s2
    lw $s3, 0($sp)     # Restore $s3
    addi $sp, $sp, 20  # Restore stack pointer

    # Return
    jr $ra

# -------------------------------------------------------------------
# Procedure: print_sum_unsign (סעיף ז)
# Description: Calculates and prints the sums of adjacent unsigned array elements.
# (array[i] + array[i+1]) for i = 0 to 8.
# Arguments:
#   $a0 - Address of the array
#   $a1 - Base (2-10)
# Uses: $s0 (loop counter i), $s1 (base), $s2 (array base address), $s3 (loop limit), $ra (saved)
# Stack: Saves $ra, $s0, $s1, $s2, $s3 (20 bytes)
# Calls: print_base, syscall (print space)
# -------------------------------------------------------------------
print_sum_unsign:
    # Stack frame setup: Save callee-saved registers and return address
    addi $sp, $sp, -20 # Allocate space for 5 registers
    sw $ra, 16($sp)    # Save return address
    sw $s0, 12($sp)    # Save $s0 (loop counter i)
    sw $s1, 8($sp)     # Save $s1 (base)
    sw $s2, 4($sp)     # Save $s2 (array base address)
    sw $s3, 0($sp)     # Save $s3 (loop limit)

    # Save arguments into callee-saved registers
    move $s2, $a0 # Array base address ($s2 holds the base address of the array)
    move $s1, $a1 # Base
    li $s0, 0     # Loop counter i = 0
    li $s3, 9     # Loop limit: array_size - 1 = 10 - 1 = 9 (Using $s3 - callee-saved)

print_sum_unsign_loop:
    # Loop condition: i < 9
    bge $s0, $s3, end_print_sum_unsign_loop # If i >= 9, end loop (Using $s3)

    # Calculate address of array[i]
    add $t1, $s2, $s0 # address of array[i] = base_address ($s2) + i ($s0) * byte_size (1)

    # Calculate address of array[i+1]
    addi $t2, $s0, 1        # calculate i+1 (in $t2)
    add $t2, $s2, $t2       # address of array[i+1] = base_address ($s2) + (i+1) ($t2)

    # Load array[i] (unsigned byte)
    lbu $t3, 0($t1) # Load byte at calculated address $t1 into $t3 (zero extended)

    # Load array[i+1] (unsigned byte)
    lbu $t4, 0($t2) # Load byte at calculated address $t2 into $t4 (zero extended)

    # Calculate sum: array[i] + array[i+1]
    add $a2, $t3, $t4 # $a2 = array[i] + array[i+1]

    # Pass base to $a1 (already saved in $s1)
    move $a1, $s1

    # Call print_base
    jal print_base

    # Print space separator
    li $v0, 4          # syscall code for print string
    la $a0, space
    syscall

    # Increment loop counter
    addi $s0, $s0, 1 # Increment loop counter i

    # Loop
    j print_sum_unsign_loop

end_print_sum_unsign_loop:
    # Restore registers
    lw $ra, 16($sp)    # Restore return address
    lw $s0, 12($sp)    # Restore $s0
    lw $s1, 8($sp)     # Restore $s1
    lw $s2, 4($sp)     # Restore $s2
    lw $s3, 0($sp)     # Restore $s3
    addi $sp, $sp, 20  # Restore stack pointer

    # Return
    jr $ra
