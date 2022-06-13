import numpy as np

coefficient = []
answer = []
count = 1;
for i in range (1, 4):
    for j in range(3):
        coefficient.append(float(input(f"Input C{count}: ")))
        count += 1
    answer.append(float(input(f"Input C{count}: ")))
    count += 1
coefficient = [coefficient[i: i + 3] for i in range(0, len(coefficient), 3)]
coefficient = np.array(coefficient)
answer = np.array(answer)
try:
    result = np.linalg.inv(coefficient).dot(answer)
except:
    print("Unable to find a solution.")
    exit(1)
print(f"Solution:\nx = {result[0]:.2f}\ny = {result[1]:.2}\nz = {result[2]:.2}")