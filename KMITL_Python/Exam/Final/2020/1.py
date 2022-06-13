def find_member_positions(number, list_of_numbers):
    pos = []
    for index, element in enumerate(list_of_numbers):
        if element == number:
            pos.append(index)
    if pos:
        return pos
    else:
        return 0

print(find_member_positions(2,[2,5,3,2,4]))  # [0, 3]
print(find_member_positions(1,[2,5,3,2,4]))  # 0