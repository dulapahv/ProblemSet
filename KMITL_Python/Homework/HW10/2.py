def bubble_sort(ArrayInput):
    ArrayLength = len(ArrayInput)
    for i in range(ArrayLength - 1):
        for j in range(0, ArrayLength - i - 1):
            if ArrayInput[j] > ArrayInput[j + 1]:
                ArrayInput[j], ArrayInput[j + 1] = ArrayInput[j + 1], ArrayInput[j]
    return ArrayInput