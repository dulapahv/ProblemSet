    .global main
main:
    MOV R1, #10
    MOV R2, #5
    MOV R3, #0
    B fnc
fnc:
    CMP R1, R2
    BGE minus
    B end
minus:
    SUB R1, R1, R2
    ADD R3, R3, #1
    B fnc
end:
    MOV R0, R3
    BX LR
