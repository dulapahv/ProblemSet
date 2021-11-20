y=input('Enter a string: ')

print('Reverse string output: ', end = '')

for x in y:
  if x.islower():
    print(x.upper(),end = "")
  elif x.isupper:
    print(x.lower(),end = "")
print(" ")