    .global main
main:
    MOV R1, #5
    MOV R0, #0
    B func
func:
    PUSH {R1, LR}
    CMP R1, #0
    BEQ end
    SUB R1, R1, #1
    BL func
end:
    POP {R1, LR}
    ADD R0, R1
    BX LR
