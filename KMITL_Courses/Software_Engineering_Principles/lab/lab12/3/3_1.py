def toHex(n):
    if n == 0:
        return "0"
    hexdigits = "0123456789ABCDEF"
    x = ""
    while n > 0:
        x = hexdigits[n % 16] + x
        n //= 16
    return x


print(toHex(0))
