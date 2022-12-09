    .global main
main:
    MOV R0, #31
    MOV R1, #15
    B fnc
fnc:
    CMP R0, R1
    BEQ end
    BLT less
    SUB R0, R0, R1
    B fnc
less:
    SUB R1, R1, R0
    B fnc
end:
    BX LR
