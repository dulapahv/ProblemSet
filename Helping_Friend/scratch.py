def f(n):
    if n >= 3:
        return (3 * f(n - 1) + 2 * f(n - 2) + f(n - 3)) % 7
    elif n == 2:
        return 3
    elif n == 1:
        return 2
    elif n == 0:
        return 1

print(f(12))