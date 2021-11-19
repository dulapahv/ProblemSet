animalNameAmountDict = {}
while True:
    usin = input("Input: ").split()
    if usin[0] == "done":
        break
    if usin[0] in animalNameAmountDict:
        animalNameAmountDict[usin[0]] += int(usin[1])
    else:
        animalNameAmountDict.update({usin[0] : int(usin[1])})

print("###Summary###")
for name, amount in animalNameAmountDict.items():
    print(f"Total Number of {name} : {amount}")