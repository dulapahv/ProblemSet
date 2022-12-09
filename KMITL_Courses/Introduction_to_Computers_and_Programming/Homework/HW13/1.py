import math

def print_btree(inputList, depth):
    for element in inputList:
        answer = '. ' * math.ceil(depth / 2) + str(element)
        print_btree(element, depth + 1) if type(element) == list else print(answer)

print_btree( [1, [[11, [111, 112]], [12, [121, [122, [1221, 1222]]]]]], 0 )