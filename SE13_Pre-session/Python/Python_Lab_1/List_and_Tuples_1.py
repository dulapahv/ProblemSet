def bubble_sort(ArrayInput):
    ArrayLength = len(ArrayInput)
    # Find how many times to loop through array
    for i in range(ArrayLength - 1):
        # Check each element from index [0]
        for j in range(0, ArrayLength - i - 1):
            # Check if element is greater than the next element (i.e. 3, 1)
            if ArrayInput[j] > ArrayInput[j + 1]:
                # Swap the element
                ArrayInput[j], ArrayInput[j + 1] = ArrayInput[j + 1], ArrayInput[j]


ArrayInput = [3, 2, 9, 7, 8]
bubble_sort(ArrayInput)
print(ArrayInput)