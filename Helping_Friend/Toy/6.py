import csv

fileName = input("Enter file name: ")
with open(fileName, "r") as file:
    data = csv.reader(file)
    team = 0
    match = 0
    point = 0
    for line in data:
        if line != "\n":
            team += 1
    print(f"Total: {team} team(s)")
    file.seek(0)
    for i, result in enumerate(data):
        print(f"team#{i+1}: played {int(result[0]) + int(result[1]) + int(result[2])} matches, received {(int(result[0]) * 3) + int(result[1])} points")

# C:\Users\Dulapah Vibulsanti\OneDrive\Documents\GitHub\ProblemSet\Helping_Friend\Toy\football.txt