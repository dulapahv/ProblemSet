nbr = input()
length = int(input())

leading = length - len(nbr)
print(f'{"0" * leading}{nbr}')
