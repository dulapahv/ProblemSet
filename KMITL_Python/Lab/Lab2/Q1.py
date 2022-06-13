sum = 0
for i in range(5):
    sum += float(input(f"Number {i+1}: "))
    avg = sum / 5
print(f"Sum: {sum}\nAverage: {avg}")