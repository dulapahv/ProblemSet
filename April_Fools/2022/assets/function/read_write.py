file = "assets/data.txt"

"""Search and Get Value in a file"""
def read_data(key):
    try:
        with open(file, "r") as readObj:
            for line in readObj:
                if key in line:
                    value = line.rstrip()
    except PermissionError:
        raise PermissionError("Permission denied")
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    try:
        return value.removeprefix(f"{key} = ")
    except UnboundLocalError:
        raise UnboundLocalError("Key not found")


"""Search and Replace Value in a file"""
def write_data(key, value):
    try:
        with open(file, "r") as readObj:
            fileData = readObj.read()
            fileData = fileData.replace(f"{key} = {read_data(key)}", f"{key} = {str(value)}")
        with open(file, "w") as writeObj:
            writeObj.write(fileData)
    except PermissionError:
        raise PermissionError("Permission denied")
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    except UnboundLocalError:
        raise UnboundLocalError("Key not found")
