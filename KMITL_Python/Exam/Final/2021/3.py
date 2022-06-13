def count_operands_in_expr(expr):
    operands = ["+", "-", "*", "/", "%", "**", "//"]
    expr = str(expr)
    if not expr:
        return 0
    else:
        operand = count_operands_in_expr(expr[1:])
        if expr[0] in operands:
            return operand + 1
        else:
            return operand

print(count_operands_in_expr((3,'**',4)))
print(count_operands_in_expr(((((2, '+', 4), '/', 3), '*', 2), '+', (3, '**', 4))))