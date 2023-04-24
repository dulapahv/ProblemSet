class InvalidArgument(Exception):
    pass


def binsearch(dataList, key):
    if not isinstance(dataList, list):
        raise InvalidArgument("dataList is not a list")

    for i in dataList:
        if not isinstance(i, int):
            raise InvalidArgument(f"{i} is not an integer")

    first = 0
    count = len(dataList)
    while 0 < count:
        step = count // 2
        mid = first + step

        if dataList[mid] < key:
            mid += 1
            first = mid
            count -= step + 1
        elif dataList[mid] > key:
            count = step
        else:
            return mid

    return None
