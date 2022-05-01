# """
# These functions allow user to read and write data from/to a file.

# The data in the files are stored as {key}={value} pairs.


# User can change how the data in the files are stored by changing the these 2 lines.
# Assuming we want to store data in the file as {key} = {value} (with spaces between the key and value), we need to change:

# `return value.removeprefix(f"{key}=")` line in the `read_data` function to `return value.removeprefix(f"{key} = ")`
# and
# `return value.removeprefix(f"{key}=")` line in the `write_data` function to `return value.removeprefix(f"{key} = ")`
# """

# """Search and Get Value in a file"""


# def read_data(file, key):
#     try:
#         with open(file, "r") as readObj:
#             for line in readObj:
#                 if key in line:
#                     value = line.rstrip()
#         return value.removeprefix(f"{key}=")
#     except PermissionError:
#         raise PermissionError("Permission denied")
#     except FileNotFoundError:
#         raise FileNotFoundError("File not found")
#     except UnboundLocalError:
#         raise UnboundLocalError("Key not found")


# """Search and Replace Value in a file"""


# def write_data(file, key, value):
#     try:
#         with open(file, "r") as readObj:
#             fileData = readObj.read()
#             fileData = fileData.replace(
#                 f"{key} = {read_data(key)}", f"{key}={str(value)}")
#         with open(file, "w") as writeObj:
#             writeObj.write(fileData)
#     except PermissionError:
#         raise PermissionError("Permission denied")
#     except FileNotFoundError:
#         raise FileNotFoundError("File not found")
#     except UnboundLocalError:
#         raise UnboundLocalError("Key not found")

# sum = 0
# for i in range(1,5+1):
#     for j in range(1,i+1):
#         sum += j + 10

# print(sum)

# sum = 0
# for i in range(1,5+1):
#     sum += j + 10

# print(sum)

# x = [i for i in range(1,5+1)]
# print(x)

from tcp_latency import measure_latency
import time

while True:
    ping = (measure_latency(host='138.91.42.107', port=25565, timeout=2.5))
    print(ping)
    time.sleep(180)