def get_average(aList):
    total_sum = sum(aList)
    return total_sum / len(aList)


score = {"Tony": [90, 65, 78, 81],
         "Tuu": [25, 75, 25, 53],
         "Anutin": [64, 76, 28, 55]}

for name, alist in score.items():
    print("Name : {:10s} score average : {:.2f}".format(name, get_average(aList)))

# score = {"Tony": [90, 65, 78, 81],
#          "Tuu": [25, 75, 25, 53],
#          "Anutin": [64, 76, 28, 55]}
# for x, y in score.items():
#     print("Name:", x + "\nscore average:", sum(y) / len(y))
