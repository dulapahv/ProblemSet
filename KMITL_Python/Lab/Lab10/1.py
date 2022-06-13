def name_list():
    nameList = []
    usin = " "
    count = 1
    while usin != "":
        usin = input(f"Enter name {count}: ")
        if usin != "":
            nameList.append(usin)
        count += 1
    print(nameList)

name_list()