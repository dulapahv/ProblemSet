studentIDScoreDict = {}
while True:
    usin = input("Enter student ID and score: ").split()
    if usin[0] == "done":
        break
    try:
        usin[0] = int(usin[0])
        usin[1] = int(usin[1])
    except:
        print("Invalid ID format!")
        continue
    if len(str(usin[0])) == 4 and 0 <= usin[1] <= 100:
        if usin[0] not in studentIDScoreDict:
            studentIDScoreDict.update({usin[0]: usin[1]})
        else:
            print("The ID is already recorded!")
    else:
        print("Invalid ID format!")
    
if not studentIDScoreDict:
    print("> no score is recorded!")
else:
    print("List:")
    for id, score in studentIDScoreDict.items():
        print(f"{id} {score}")
    amount = len(studentIDScoreDict)
    avg = sum(studentIDScoreDict.values()) / amount
    print(f"There are {amount} student(s). The average score is {avg} points.")