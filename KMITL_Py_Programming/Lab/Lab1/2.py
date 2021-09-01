def swap(a, b):
    a, b = b, a
    return a, b

def isEqual(a, b):
    return True if a==b else False

print(swap(1,2))
print(isEqual(3,6))
print(isEqual(3,3))
