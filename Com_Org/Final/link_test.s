    .global main
main:
    MOV R0, #0
    B fnc
fnc:
    PUSH {LR}
    BL fnc2
    POP {LR}
    BX LR
fnc2:
    PUSH {LR}
    ADD R0, R0, #10
    BL fnc3
    POP {LR}
    BX LR
fnc3:
    ADD R0, R0, #2
    BX LR
