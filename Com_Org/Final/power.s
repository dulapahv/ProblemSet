    .global main
main:
    MOV R1, #2
    MOV R2, #3
    B fnc
fnc:
    CMP R2, #1
    BEQ end
    MUL R1, R1, R1
    SUB R2, R2, #1
    B fnc
end:
    MOV R0, R1
    BX LR
