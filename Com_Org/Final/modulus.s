    .global main
main:
    MOV R1, #10
    MOV R2, #3
    B fnc
fnc:
    CMP R1, R2
    BGE minus
    B end
minus:
    SUB R1, R1, R2
    B fnc
end:
    MOV R0, R1
    BX LR
