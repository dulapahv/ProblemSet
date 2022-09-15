	.data
	.balign 4
	question: .asciz "What is your favorite number?"

	.balign 4
	message: .asciz "%d is a great number \n"

	.balign 4
	pattern: .asciz "%d"

	.balign 4
	number: .word 0

	.balign 4
	lr_bu: .word 0

	.text @ Text segment begins here

	@ Used by the compiler to tell libc where main is located
	.global main
	.func main

main:
	@ Backup the value inside Link Register
	LDR R1, addr_lr_bu
	STR lr, [R1] @ Mem[addr_lr_bu] <- LR

	@ Load and print question
	LDR R0, addr_question
	BL printf

	@ Define pattern to scanf and where to store number
	LDR R0, addr_pattern
	LDR R1, addr_number
	BL scanf

	@ Print the message with number
	LDR R0, addr_message
	LDR R1, addr_number
	LDR R1, [R1]
	BL printf

	@ Load the value of lr_bu to LR
	LDR lr, addr_lr_bu
	LDR lr, [lr] @ LR <- Mem[addr_lr_bu]
	BX lr

@ Define addresses of variables
addr_question: .word question
addr_message: .word message
addr_pattern: .word pattern
addr_number: .word number
addr_lr_bu: .word lr_bu

@ Declare printf and scanf functions to be linked with
.global printf
.global scanf
