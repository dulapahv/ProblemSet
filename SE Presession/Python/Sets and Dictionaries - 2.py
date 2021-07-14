score = {"Tony": [90, 65, 78, 81],
         "Tuu": [25, 75, 25, 53],
         "Anutin": [64, 76, 28, 55]}
for x, y in score.items():
    print("Name:", x + "\nscore average:", sum(y) / len(y))
