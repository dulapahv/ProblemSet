emplist = dict()

while(1):
    command = input("Enter command: ")
    if command == "lookup":
        for key in emplist:
            print(key, emplist[key])
    elif command == "add":
        id = input("Enter id: ")
        name = input("Enter name: ")
        emplist[id] = name
    elif command == "remove":
        id = input("Enter id: ")
        del emplist[id]
    elif command == "search":
        id = input("Enter id: ")
        if id in emplist:
            print(id, emplist[id])
        else:
            print("Not found")
    elif command == "quit":
        break
