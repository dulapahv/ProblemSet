def display_f(n):
    if n == 0:
        print(0)
        return 0
    if n > 0 and n % 2 == 0:
        print(2 * display_f(n/2) + 1)
        return 2 * display_f(n/2) + 1
    else:
        print(0)
        return 0

display_f(4)
