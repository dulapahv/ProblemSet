pPig = ["Peppap", "George", "Emily", "Candy", "Danny", "Freddy", "Gerald"]
length = len(pPig)
newP = []
for p in range(length-1, 0 ,-1):
    if len(pPig[p]) % 2 == 0:
        newP.append(pPig[p])
for p in newP:
    print(f"{p} ", end="")