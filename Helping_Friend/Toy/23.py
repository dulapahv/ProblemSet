def swap(a):
    for i in range(len(a) -1):
        temp = a[i]
        a[i] = a[i + 1]
        a[i + 1] = temp
    return a

a = [1,2,3,4,5]
print(swap(a))