string = "book,dog,drink,rain,pen"
for i in range(len(string)):
    if string[i] == ',':
        print('')
    else:
        print(string[i], end = '')