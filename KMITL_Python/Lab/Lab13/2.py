def list_reverse(list):
    if len(list) == 0: 
        return []
    return [list[-1]] + list_reverse(list[:-1])

print(list_reverse([1,2,3]))