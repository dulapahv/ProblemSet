	.data
primes:
	.word 2
	.word 3
	.word 5
	.word 7
	
	.text
	.global main
main:
	LDR R3, =primes @ Load the address for the data in R3
	LDR R0, [R3, #4] @ Get the next item in the list
end:
	BX LR
