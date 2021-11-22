def list_member(num, list):
    if len(list) == 0:
        return False
    if num == list[0]:
        return True
    else:
        list = list[1:]
        return list_member(num, list)

print(list_member(2, [1,2,3]))