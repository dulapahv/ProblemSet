    .global main
main:
    MOV R1, #5
    MOV R0, #1
    B func
func:
    PUSH {R1, LR}
    CMP R1, #1
    BEQ end
    SUB R1, R1, #1
    BL func
end:
    POP {R1, LR}
    MUL R0, R1
    BX LR
