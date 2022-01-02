file = open("Helping_Friend/Nono/books.txt", "r")

# for line in file.readlines():
#     print(f"{line.strip()[0]}{len(line.strip())}")

print(*[f"{line.strip()[0]}{len(line.strip())}" for line in file.readlines()], sep="\n")

file.close()