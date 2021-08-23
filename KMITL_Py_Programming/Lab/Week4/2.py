char = input("Please enter a character: ")
charHex = hex(ord(char)).removeprefix("0x")
print(f'The Unicode of "{char}" is u00{charHex}.')