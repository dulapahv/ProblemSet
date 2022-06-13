list1 = [45,44,100,12,561]
new_list=[]
for c in list1:
    if c%2 == 0:
        new_list.append(c)
    elif c > 100:
        new_list.append(c//2)
    else:
        new_list.append(c%2)
print(new_list)