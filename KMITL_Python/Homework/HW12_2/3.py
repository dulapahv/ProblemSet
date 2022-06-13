def product(*sets):
    cartesianList = []
    for i in range(len(sets)):
        if i == 0:
            cartesianList = [(j,) for j in sets[i]]
        else:
            cartesianList = [n + (m,) for n in cartesianList for m in sets[i]]
    return cartesianList

# s1 = set([1,2,3])
# s2 = set(['p','q'])
# s3 = set(['a','b','c'])

# print(product(s1,s2))
# print(product(s1, s2, s3))
# print(product(s1))