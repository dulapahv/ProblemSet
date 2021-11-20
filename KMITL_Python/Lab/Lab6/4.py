def sum_of_digit(number):
    total = 0
    for num in number:
        total += int(num)
    return total

usin = input("Input number: ")
print(f"Sum of digits: {sum_of_digit(usin)}")
