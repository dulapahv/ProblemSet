#sort a list based on the value of the third element in the sublist

def sort_list(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i][2] > list[j][2]:
               list[i], list[j] = list[j], list[i]
    return list

# def sort_list(l):
#     return sorted(l, key=lambda x: x[2])

l = [[1,2,99],[4,5,6],[7,8,9]]

print(sort_list(l))