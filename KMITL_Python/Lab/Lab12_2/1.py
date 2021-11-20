print("Phonebook Manager")
print("Press “+” to add a new contact.")
print("Press “-” to delete a contact.")
print("Press “f” to find a contact.")
print("Press “p” to print out all contacts in the phonebook.")
print("Press “q” to quit the program.")

phoneBook = {}

choice = input("What would you like to do\nchoice --> ")
while (choice != "q"):
    if choice == "+":
        name = input("\nEnter name: ")
        number = int(input("Enter number: "))
        phoneBook.update({name: number})
    elif choice == "-":
        name = input("\nEnter name: ")
        phoneBook.pop(name) if name in phoneBook else print("Name not found!")
    elif choice == "f":
        name = input("\nEnter name: ")
        print(phoneBook[name]) if name in phoneBook else print("Name not found!")
    elif choice == "p":
        for name, number in phoneBook.items():
            print(f"{name} - {number}")
    else:
        print("\nPlease select a valid choice!")

    choice = input("\nWhat would you like to do\nchoice --> ")