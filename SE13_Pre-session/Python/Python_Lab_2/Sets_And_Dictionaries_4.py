def get_subsets(fullset):
    listrep = list(fullset)
    subsets = []
    for i in range(2 ** len(listrep)):
        subset = []
        for k in range(len(listrep)):
            if i & 1 << k:
                subset.append(listrep[k])
        subsets.append(subset)
    return subsets


subsets = get_subsets(set([1, 2, 3, ]))
print(subsets)
print(len(subsets))
