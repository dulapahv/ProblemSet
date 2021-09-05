def test(name, x, y):
    print(name, x, y)

list = [["account", 500, 600], ["bg", 200, 600]]
for i in range(len(list)):
    test(list[i][0], list[i][1], list[i][2])


list = [["account", 400, 600], ["bg", 400, 600]]
for i in range(len(list)):
    test(list[i][0], list[i][1], list[i][2])