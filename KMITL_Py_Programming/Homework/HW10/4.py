def print_table(tableList):
    columnWidth = max(len(word) for row in tableList for word in row) + 2
    for row in tableList:
        print("".join(word.ljust(columnWidth) for word in row))