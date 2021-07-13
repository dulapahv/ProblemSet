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

# Another solution using loop
# lst1 = [3, 1, 2, 7]
# lst2 = [4, 1, 2, 5]
#
#
# def my_union(lst1, lst2):
#     union = []
#     all_list = [lst1, lst2]
#     for i in range(2):
#         for members in all_list[i]:
#             if members not in union:
#                 union.append(members)
#
#     return union
#
#
# def my_intersection(lst1, lst2):
#     intersect = []
#     for i in lst1:
#         for j in lst2:
#             if i == j and i not in intersect:
#                 intersect.append(i)
#
#     return intersect
#
#
# def my_difference(lst1, lst2):
#     difference = []
#     intersect = my_intersection(lst1, lst2)
#     for member in lst1:
#         if member not in intersect:
#             difference.append(member)
#
#    return difference
#
#
# print(my_union(lst1, lst2))
# print(my_intersection(lst1, lst2))
# print(my_difference(lst1, lst2))