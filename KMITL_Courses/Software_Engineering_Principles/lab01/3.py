def binary_search(target: int, arr: list[int], start: int = 0, end: int | None = None) -> int | bool:
    # end not given, set it to length of array
    if end is None:
        end = len(arr)
    # if the adjusted pivot is beyond array size, return False
    if start >= len(arr) or end < 0:
        return False
    # check base case
    if start > end:
        return False
    # calculate mid
    mid = (start + end) // 2
    # check if the target is at mid
    if arr[mid] == target:
        return mid
    # check if target < mid
    elif target < arr[mid]:
        return binary_search(target, arr, start, mid-1)
    # target > mid
    else:
        return binary_search(target, arr, mid+1, end)


print(binary_search(12, [0, 2, 4, 6, 8, 10]))
