def composite(dict1, dict2):
    dict3 = {}
    for dict1Key in dict1:
        for dict2Key in dict2:
            if dict2Key == dict1[dict1Key]:
                dict3[dict1Key] = dict2[dict2Key]
    return dict3

# dict1 = {'a':'p', 'b':'r', 'c':'q', 'd':'p', 'e':'s'}
# dict2 = {'p':'1', 'q':'2', 'r':'3'}
# print(composite(dict1, dict2))