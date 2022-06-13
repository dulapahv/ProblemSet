a = [element for element in input("Input: a = ") if element.isnumeric()]
b = [element for element in input("Input: b = ") if element.isnumeric()]
if len(a) == len(b):
    dotProduct = 0
    for i in range(len(a)):
        dotProduct += int(a[i]) * int(b[i])
    print(f"Output: {dotProduct:.1f}")
else:
    print("Output: Invalid input")