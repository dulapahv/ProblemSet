def FindDistance(InputNode):
    if node[InputNode][0] is None:
        return node[InputNode][1]
    else:
        result = node[InputNode][1] + node[node[InputNode][0]][1]
        return result


node = {"A": ["C", 110],
        "B": ["D", 840],
        "C": ["E", 450],
        "D": [None, 0],
        "E": [None, 0]}

StartNode = input("Enter Node: ")
print("total distance:", float(FindDistance(StartNode)), "Km.")
