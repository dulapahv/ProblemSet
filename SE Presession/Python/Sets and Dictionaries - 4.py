def FindPowerset(InputSet):
    result = []
    for i in range(2 ** len(InputSet)):
        subset = []
        for k in range(len(InputSet)):
            if i & 1 << k:
                subset.append(InputSet[k])
        result.append(subset)
    return result


set = FindPowerset([1, 2])
print(set)
