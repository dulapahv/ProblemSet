	.data
	@ Define all the strings and variables
	.balign 4
	get_num_1: .asciz "Number 1 :\n"

	.balign 4
	get_num_2: .asciz "Number 2 :\n"

	@ printf and scanf use %d in decimal numbers
	.balign 4
	pattern: .asciz "%d"

	@ Declare and initialize variables: num_1 and num_2
	.balign 4
	num_1: .word 0

	.balign 4
	num_2: .word 0

	@ Output message pattern
	.balign 4
	output: .asciz "Resulf of %d + %d = %d\n"

	@ Variables to backup link register
	.balign 4
	lr_bu: .word 0

	.balign 4
	lr_bu_2: .word 0

	.text
sum_func:
	@ Save (Store) Link Register to lr_bu_2
	LDR R2, addr_lr_bu_2
	STR lr,[R2] @ Mem[addr_lr_bu_2] <- LR

	@ Sum values in R0 and R1 and return in R0
	ADD R0, R0, R1

	@ Load Link Register from back up 2
	LDR lr, addr_lr_bu_2
	LDR lr, [lr] @ LR <- Mem[addr_lr_bu_2]
	
	BX lr

	@ address of Link Register back up 2
	addr_lr_bu_2: .word lr_bu_2

	@ main function
	.global main

main:
	@ Store (back up) Link Register
	LDR R1, addr_lr_bu
	STR lr, [R1] @ Mem[addr_lr_bu] <- LR

	@ Print Number 1 :
	LDR R0, addr_get_num_1
	BL printf

	@ Get num_1 from user via keyboard
	LDR R0, addr_pattern
	LDR R1, addr_num_1
	BL scanf

	@ Print Number 2 :
	LDR R0, addr_get_num_2
	BL printf

	@ Get num_2 from user via keyboard
	LDR R0, addr_pattern
	LDR R1, addr_num_2
	BL scanf

	@ Pass values of num_1 and num_2 to sum_func
	LDR R0, addr_num_1
	LDR R0, [R0] @ R0 <- Mem[addr_num_1]
	LDR R1, addr_num_2
	LDR R1, [R1] @ R1 <- Mem[addr_num_2]
	BL sum_func

	@ Copy returned value from sum_func to R3
	MOV R3, R0 @ to printf

	@ Print the output message, num_1, num_2 and result
	LDR R0, addr_output
	LDR R1, addr_num_1
	LDR R1, [R1]
	LDR R2, addr_num_2
	LDR R2, [R2]
	BL printf

	@ Restore Link Register to return
	LDR lr, addr_lr_bu
	LDR lr, [lr] @ LR <- Mem[addr_lr_bu]
	BX lr
	
@ Define pointer variables
addr_get_num_1: .word get_num_1
addr_get_num_2: .word get_num_2
addr_pattern: .word pattern
addr_num_1: .word num_1
addr_num_2: .word num_2
addr_output: .word output
addr_lr_bu: .word lr_bu

@ Declare printf and scanf functions to be linked with
.global printf
.global scanf
