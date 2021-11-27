import tkinter as tk
from tkinter import filedialog

urlList = []

while True:
    print("A URL Favorite Manager")
    print('Press “+” to add a new URL ')
    print('Press “–” to delete a URL.')
    print('Press “i” to get a URL by specifying its index of the list.')
    print('Press “s” to save the URL list to a file.')
    print('Press “l” to load previous saved URL list from a file.')
    print('Press “p” to print out all URLs in the list.')
    print('Press “q” to quit the program.')

    choice = input("Enter command: ")
    
    if (choice == "+"):
        usin = input("Enter URL to add: ")
        if usin not in urlList:
            urlList.append(usin)
        else:
            print("That URL already exists!")

    elif (choice == "-"):
        usin = input("Enter URL to remove: ")
        if usin in urlList:
            urlList.remove(usin)
        else:
            print("That URL does not exists!")

    elif (choice == "i"):
        usin = int(input("Enter index: "))
        try:
            print(urlList[usin])
        except IndexError:
            print("Index out of range!")

    elif (choice == "s"):
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        filePath = filedialog.asksaveasfilename(filetypes=[("Text Files", ".txt")])
        file = open(filePath, "w")
        for url in urlList:
            file.write(f"{url}\n")
        file.close()

    elif (choice == "l"):
        while True:
            usin = input("Enter file name: ")
            try:
                file = open(usin, "r")
            except FileNotFoundError:
                print("File not found!")
                continue
            break
        file = open(usin, "r")
        urlList.clear()
        for line in file:
            urlList.append(line)
        file.close()
    elif (choice == "p"):
        for url in urlList:
            print(url)

    elif (choice == "q"):
        exit(0)

    else:
        print("Please enter a valid command!")
    print()

# C:/Users/Dulapah Vibulsanti/OneDrive/Documents/GitHub/ProblemSet/KMITL_Python/Lab/Lab14/urlBookmark.txt