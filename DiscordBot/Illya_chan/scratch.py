usin = input()

# Get index of previous operand and current operand
operandIndex = []
previousOperandIndex = 0
operandCount = 0
for i in range(len(usin)):
    if usin[i] == '+' or usin[i] == '-':
        operandIndex.append(list())
        operandIndex[operandCount].append(previousOperandIndex)
        operandIndex[operandCount].append(i)
        previousOperandIndex = i
        operandCount += 1

# Slice the input based on operand index list
termList = []
for i in range(len(operandIndex)):
    termList.append(usin[operandIndex[i][0]:operandIndex[i][1]])
termList.append(usin[operandIndex[len(operandIndex) - 1][1]:])
print(termList)

# # Reduce exponential value by 1
# def differentiate():
#     diffTerm = termList
#     for index, term in enumerate(diffTerm):
#         diffTerm[index] = term.replace("^" + str(len(diffTerm) - index - 1), "^" + str(len(diffTerm) - index - 2))
#     diffTerm[len(diffTerm) - 3] = diffTerm[len(diffTerm) - 3].replace("^1", "")
#     diffTerm[len(diffTerm) - 2] = diffTerm[len(diffTerm) - 2].replace("x", "") 
#     diffTerm.pop(len(diffTerm) - 1)
#     return ''.join(char for char in diffTerm)

# # Increase exponential value by 1
# def integrate():
#     intTerm = termList
#     for index, term in enumerate(intTerm):
#         intTerm[index] = term.replace("^" + str(len(intTerm) - index - 1), "^" + str(len(intTerm) - index))
#     intTerm[len(intTerm) - 2] = intTerm[len(intTerm) - 2].replace("x", "x^2")
#     intTerm[len(intTerm) - 1] = intTerm[len(intTerm) - 1] + "x"
#     intTerm.append("+c")
#     return ''.join(char for char in intTerm)

# print(differentiate())
#print(integrate())