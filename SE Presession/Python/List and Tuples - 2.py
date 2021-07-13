def my_union(list1, list2):
    result = list(list1)
    result.extend(x for x in list2 if x not in result)
    return result


def my_intersection(list1, list2):
    result = [x for x in list1 if x in list2]
    return result


def my_difference(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result


list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

print(my_union(list1, list2))
print(my_intersection(list1, list2))
print(my_difference(list1, list2))

# Another solution by using set()
# list1 = [3, 1, 2, 7]
# list2 = [4, 1, 2, 5]
#
# my_union = list1 + list2
# print(my_union)
#
# my_intersection = set(list1) & set(list2)
# print(my_intersection)
#
# my_difference = set(list1) - set(list2)
# print(my_difference)