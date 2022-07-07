# """
# These functions allow user to read and write data from/to a file.

# The data in the files are stored as {key}={value} pairs.


# User can change how the data in the files are stored by changing the these 2 lines.
# Assuming we want to store data in the file as {key} = {value} (with spaces between the key and value), we need to change:

# `return value.removeprefix(f"{key}=")` line in the `read_data` function to `return value.removeprefix(f"{key} = ")`
# and
# `return value.removeprefix(f"{key}=")` line in the `write_data` function to `return value.removeprefix(f"{key} = ")`
# """

# """Search and Get Value in a file"""


# def read_data(file, key):
#     try:
#         with open(file, "r") as readObj:
#             for line in readObj:
#                 if key in line:
#                     value = line.rstrip()
#         return value.removeprefix(f"{key}=")
#     except PermissionError:
#         raise PermissionError("Permission denied")
#     except FileNotFoundError:
#         raise FileNotFoundError("File not found")
#     except UnboundLocalError:
#         raise UnboundLocalError("Key not found")


# """Search and Replace Value in a file"""


# def write_data(file, key, value):
#     try:
#         with open(file, "r") as readObj:
#             fileData = readObj.read()
#             fileData = fileData.replace(
#                 f"{key} = {read_data(key)}", f"{key}={str(value)}")
#         with open(file, "w") as writeObj:
#             writeObj.write(fileData)
#     except PermissionError:
#         raise PermissionError("Permission denied")
#     except FileNotFoundError:
#         raise FileNotFoundError("File not found")
#     except UnboundLocalError:
#         raise UnboundLocalError("Key not found")

# sum = 0
# for i in range(1,5+1):
#     for j in range(1,i+1):
#         sum += j + 10

# print(sum)

# sum = 0
# for i in range(1,5+1):
#     sum += j + 10

# print(sum)

# x = [i for i in range(1,5+1)]
# print(x)

# from tcp_latency import measure_latency
# import time

# while True:
#     ping = (measure_latency(host='138.91.42.107', port=25565, timeout=2.5))
#     print(ping)
#     time.sleep(180)


# class BetterList:
#     def __init__(self, *args):
#         self.list = list(args)

#     def __add__(self, other):
#         return BetterList(self.list + other.list)

#     def __str__(self):
#         return str(self.list)

#     def __getitem__(self, index):
#         return self.list[index]

#     def __setitem__(self, index, value):
#         self.list[index] = value

#     def __len__(self):
#         return len(self.list)

#     def __delitem__(self, index):
#         del self.list[index]

#     def __iter__(self):
#         return iter(self.list)

#     def __reversed__(self):
#         return reversed(self.list)

#     def __contains__(self, item):
#         return item in self.list

#     def __eq__(self, other):
#         return self.list == other.list

#     def __ne__(self, other):
#         return self.list != other.list

#     def __gt__(self, other):
#         return self.list > other.list


# list1 = BetterList(1,2,3)
# list2 = BetterList(4,5,6)

# print(list1 + list2)
# print(list1)

# class Card:
#     def __init__ (self, value, suit):
#         self.v = value
#         self.s = suit

#     def __str__ (self):
#         return "(" + self.v + " " + self.s + ")"

#     def getScore(self):
#         pairs = {"A": 1, "2": 2, "3": 3, "4": 4,
#                  "5": 5, "6": 6, "7": 7, "8": 8,
#                  "9": 9, "10": 10}
#         if self.v in ["J", "Q", "K"]:
#             return pairs["10"]
#         return pairs[self.v]

#     def sum(self, other):
#         return (self.getScore() + other.getScore()) % 10

#     def __lt__ (self, rhs):
#         faces = {"3": 10, "4": 20, "5": 30, "6": 40,
#                  "7": 50, "8": 60, "9": 70, "10": 80,
#                  "J": 90, "Q": 100, "K" : 110, "A": 120,
#                  "2": 130}
#         suits = {"club": 1, "diamond": 2, "heart": 3,
#                  "spade": 4}
#         return (faces[self.v] + suits[self.s]) < (faces[rhs.v] + suits[rhs.s])

# n = int(input())

# cards = []

# for i in range(n):
#     value, suit = input().split()
#     cards.append(Card(value, suit))

# for i in range(n):
#     print(cards[i].getScore())

# print("-" * 10)

# for i in range(n - 1):
#     print(Card.sum(cards[i], cards[i+1]))

# print("-" * 10)


# cards.sort()

# for i in range(n):
#     print(cards[i])


# # Euler method python program

# # function to be solved
# def f(x,y):
#     return x+y

# # or
# # f = lambda x: x+y

# # Euler method
# def euler(x0,y0,xn,n):

#     # Calculating step size
#     h = (xn-x0)/n

#     print('\n-----------SOLUTION-----------')
#     print('------------------------------')
#     print('x0\ty0\tslope\tyn')
#     print('------------------------------')
#     for i in range(n):
#         slope = f(x0, y0)
#         yn = y0 + h * slope
#         print('%.4f\t%.4f\t%0.4f\t%.4f'% (x0,y0,slope,yn) )
#         print('------------------------------')
#         y0 = yn
#         x0 = x0+h

#     print('\nAt x=%.4f, y=%.4f' %(xn,yn))

# # Inputs
# print('Enter initial conditions:')
# x0 = float(input('x0 = '))
# y0 = float(input('y0 = '))

# print('Enter calculation point: ')
# xn = float(input('xn = '))

# print('Enter number of steps:')
# step = int(input('Number of steps = '))

# # Euler method call
# euler(x0,y0,xn,step)

# import math
# x = math.e ** (0.0004 ** 2)
# print(f"{x:.10f}")

# def solve(h, x=0.4):
#     x0 = x - h  # find x0
#     y0 = 1 + (x0 * (0 * (1 ** 0.5)))  # find y(x0)
#     return 1 + (h * (x0 * (y0 ** 0.5)))

# print(solve(0.0004))

# // pseudocode
#  function powmod(base b, exponent e, modulus m)
#   if m = 1 then return 0
#   var c := 1
#   for var a from 1 to e
#     c := (c * b) mod m
#   end for
#   return c

# def powmod(base, expo, modulus):
#     if modulus == 1:
#         return 0
#     c = 1
#     for i in range(1, expo + 1):
#         print(f'{c} * {base} % {modulus} = {c * base % modulus}')
#         c = (c * base) % modulus
#     return c

# print(powmod(6036982461, 21345, 23))

# height = int(input())
# for i in range(height):
#     print(' ' * (height - i - 1), end='')
#     print('*' * ((2 * i) + 1), end='')
#     print()

# data = []
# for i in range(5):
#     data.append(input())

# score = int(input())

# if score >= 90:
#     print('A')
# elif score >= 85 and score <= 89:
#     print('B+')
# elif score >= 80 and score <= 84:
#     print('B')
# elif score >= 75 and score <= 79:
#     print('C+')
# elif score >= 70 and score <= 74:
#     print('C')
# elif score >= 65 and score <= 69:
#     print('D+')
# elif score >= 60 and score <= 64:
#     print('D')
# else:
#     print('F')

# height = int(input())
# for i in range(height):
#     print(' ' * (height - i - 1), end='')
#     print('*' * ((2 * i) + 1), end='')
#     print()
# for i in range(height - 1):
#     print(' ' * (i + 1), end='')
#     print('*' * (2 * (height - i - 1) - 1), end='')
#     print()

# column = int(input())
# row = int(input())

# mat = []
# for i in range(row * column):
#     mat.append(float(input()))

# for i in range(row):
#     for j in range(column):
#         result = (mat[i * column + j] - min(mat)) / (max(mat) - min(mat))
#         print(f"{result:.4f}", end=' ')
#     print()

# string = input()

# for i in range(len(string)):
#     print(' ' * (len(string) - i - 1) + string[i], end='')
#     print()

# n = int(input())
# data = []
# for i in range(n):
#     data.append(int(input()))

# x = 1
# while True:
#     if len(data) <= (2 ** x):
#         break
#     x += 1

# print(x)

# import math
# sum = 0
# for i in range(0, 101):
#     print(i)
#     sum += math.floor(i/5)

# print(sum)

# import math
# try:
#     for i in range(1, 101):
#         for y in range(-99999, 99999):
#             if (i / y) - 1 == -1:
#                 print(f"{y = }")
#                 break
# except:
#     pass

# import math
# sum = 0
# for i in range(0, 11):
#     sum += (math.factorial(10)) / (math.factorial(i) * math.factorial(10 - i))

# print(sum)

"""
>>> factorial(5)
120

>>> [factorial(n) for n in range(6)]
[1, 1, 2, 6, 24, 120]

>>> factorial(30)
265252859812191058636308480000000

>>> factorial(-1)
Traceback (most recent call last):
    ...
ValueError: n must be >= 0

>>> factorial(30.1)
Traceback (most recent call last):
    ...
ValueError: n must be exact integer

>>> factorial(30.0)
265252859812191058636308480000000


>>> factorial(1e100)
Traceback (most recent call last):
    ...
OverflowError: n too large
"""

# def factorial(n):
#     import math
#     if not n >= 0:
#         raise ValueError("n must be >= 0")
#     if math.floor(n) != n:
#         raise ValueError("n must be exact integer")
#     if n+1 == n:  # catch a value like 1e300
#         raise OverflowError("n too large")
#     result = 1
#     factor = 2
#     while factor <= n:
#         result *= factor
#         factor += 1
#     return result

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

# from chadchart import Policy
# policy = Policy()
# policy.show_all()
# print('All policy:',policy.all)
# print('-----')
# print('Number 1 (dictionary):', policy.number(1))
# print('Number 1 (thai):',policy.number(1)['thai'])
# print('Number 1 (english):',policy.number(1)['english'])
# print('Number 1 (tag):', policy.number(1)['tag'])
# print(policy.all_tag)
# print(policy.all_tag['เรียนดี'])
# policy.show_category()
# policy.category('ปลอดภัยดี')
# policy.credit()
# policy.developer()

# def find_avg(data):
#     try:
#         return sum(data) / len(data)
#     except ZeroDivisionError:
#         raise Exception("Cannot find average of empty data!")
#     except TypeError:
#         raise Exception("Data type not supported!")

# print(find_avg([1, 2, 3, 4, 5]))

# print('Hello world!')
# a = 2
# a **= 3
# print(a)

# num1 = 10 * 20
# num2 = 12.34
# num3 = 0.55
# num4 = -.65
# text1 = 'Gacha player will never be happy'
# bool1 = True

# print(num1)
# print(text1)
# print(bool1)

# string1 = 'The fact that you are ugly is what makes you a failure'
# string2 = "Will you accept half of my chromosome?"
# stringQuote1 = 'He told me, "Even Hitler cared Germany, but no one care me" before he disappeared.'
# stringQuote2 = "Stop 'coding' and go get a 'life'!"

# print(string1.title())
# print(string2.upper())
# print(stringQuote1.lower())


# firstName = 'Konomi'
# lastName = 'Suzuki'
# print(firstName + ' ' + lastName)
# print(firstName, lastName)
# print('%s %s' % (firstName, lastName))
# print('{} {}'.format(firstName, lastName))

# print(f'{firstName} {lastName}')

# print('Sometimes it takes a real man to become\nthe best girl')
# print('Sometimes it takes a\t\treal man to become the best girl')

# var = '+ Uwooo +'

# print(f'{var.lstrip("+")}')
# print(f'{var.rstrip("+")}')
# print(f'{var.strip("+")}')

# I'll always have a special place in your heart, even I'm just a comment.

# """
# At times, our relationship felt like it was the best
# thing that had ever happened to me, but lately,
# everything has felt wrong.
# """

# x = 10.6
# print(int(x))

# girlfriends = ['Armstrong', 'Phoenix', 'Chadchart']
# girlfriends.insert(1, 'Anya')
# print(girlfriends)

# lover = []

# secret = ['you', 'me', 'bed', 'now']
# secret2 = [10, 20, 30]
# print(sorted(secret))
# print(sorted(secret, reverse=True))
# secret2.sort(reverse=True)
# print(secret2)

# txt = 'ara~'
# print(len(txt))

# msg1 = input()
# msg2 = input('May I use your toilet? ')
# msg3 = input('Give me a number: ').split(', ')
# print(msg1)
# print(msg2)
# print(msg3)

# msg = ['our', 'love', 'is', 'like', 'a', 'pi']
# removed = msg.pop(1)
# print(removed)
# print(msg)

# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(num[:5])          # [0, 1, 2, 3, 4]
# print(num[5:])          # [5, 6, 7, 8, 9]
# print(num[2:4])         # [2, 3]
# print(num[:-2])         # [0, 1, 2, 3, 4, 5, 6, 7]
# print(num[-2:])         # [8, 9]
# print(num[-4:-2])       # [6, 7]
# print(num[:8:2])        # [0, 2, 4, 6]
# print(num[1:8:2])       # [1, 3, 5, 7]
# print(num[::-1])        # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(num[::-2])        # [9, 7, 5, 3, 1]
# print(num[:])           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ans = [1, 3, 2, 3, 5, 4]
# sus = ans[:]
# print(sus)


# print(list(range(10)))          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(5, 10)))       # [5, 6, 7, 8, 9]
# print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]

# for i in range(10):
#     print(i)

# square = []
# for number in range(10):
#     square.append(number**2)
# print(square)

# square = [number**2 for number in range(10)]
# print(square)

# people = ['Chocola', 'Vanilla', 'Maple']
# new_list = []
# for person in people:
#     new_list.append(f'Ms.{person}')
# for person in new_list:
#     print(person)

# people = ['Chocola', 'Vanilla', 'Maple']
# new_list = [f'Ms.{person}' for person in people]
# for person in new_list:
#     print(person)

# txt = "weed"
# print(list(txt))

# txt = "weed"
# for char in txt:
#     print(char)

# txt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(txt[0])           # A
# print(txt[-1])          # Z
# print(txt[:5])          # ABCDE
# print(txt[5:])          # FGHIJKLMNOPQRSTUVWXYZ
# print(txt[::2])         # ACEGIKMOQSUWY
# print(txt[1::2])        # BDFHJLNPRTVXZ
# print(txt[-4:-2])       # WX
# print(txt[1:10:2])      # BDFHJ
# print(txt[::-1])        # ZYXWVUTSRQPONMLKJIHGFEDCBA
# print(txt[::-2])        # ZXVTRPNLJHFDB
# print(txt[:])           # ABCDEFGHIJKLMNOPQRSTUVWXYZ

# txt = 'Love will guide the way, our hearts bound by an eternal promise!'
# check1 = 'promise' in txt
# check2 = 'hate' in txt
# print(check1)
# print(check2)

# txt = "Don't cry because it's over, smile because it happened."
# print(txt.find('because'))      # First occurrence
# print(txt.rfind('because'))     # Last occurrence

# txt = 'never gonna give you up, never gonna let you down'
# count = txt.count('never')
# print(count)

# txt = 'From this day forth, our fates are bound together'
# txt = txt.split(' ')
# print(txt)

# txt = ('yes', 'we', 'can')
# for word in txt:
#     print(word)

# val_int = 1112
# print(f'{val_int:b}')       # 10001011000
# print(f'{val_int:e}')       # 1.112000e+03
# print(f'{val_int:.2e}')     # 1.11e+03

# val_float = 1112.12345
# print(f'{val_float:.3e}')     # 1.112e+03
# print(f'{val_float:.4f}')     # 1112.1235
# print(f'{val_float:.2%}')     # 111212.35%

# txt = 'SE14 Pre-Session'
# print(f'+{txt:>40}+')
# print(f'+{txt:<40}+')
# print(f'+{txt:^40}+')
# print(f'+{txt:*>40}+')
# print(f'+{txt:=<40}+')
# print(f'+{txt:#^40}+')

# give example of set and mathematical operation
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1 & set2)      # Intersection                      {1, 2}
# print(set1 | set2)      # Union                             {1, 2, 3, 4, 5, 6, 7, 8}
# print(set1 - set2)      # Difference                        {3, 4, 5}
# print(set1 ^ set2)      # Symmetric difference              {3, 4, 5, 6, 7, 8}
# print(set1 >= set2)     # Is set2 a subset of set1?         False
# print(set1 <= set2)     # Is set1 a subset of set2?         False
# print(set1 == set2)     # Are set1 and set2 equal?          False
# print(set1 != set2)     # Are set1 and set2 not equal?      True

# x = 5
# if x == 5:
#     print('x is 5')
# print('done')

# x = 6
# if x == 5:
#     print('x is 5')
# else:
#     print('x is 6')
# print('done')

# x = 10
# if x == 5:
#     print('x is 5')
# elif x == 6:
#     print('x is 6')
# else:
#     print('x is not 5 or 6')
# print('done')

# txt = 'I love Genshin Impact'
# print('money' in txt)

# number = [1, 2, 3, 4, 5]
# print(1 in number)

# x = 5
# if x >= 0 and x < 10:
#     print('nice')
# elif (x >= 10 and x < 20) or (x == 3):
#     print('bruh')
# else:
#     print('no')

# x = 0
# while x < 5:
#     print(x)
#     x += 1

# for x in range(5):
#     print(x)

# txt1 = 'I hate'
# txt2 = 'gacha game'
# print(txt1, txt2, sep='+-+')

# number = []
# num = ''
# while num != 'quit':
#     num = input('Enter a number: ')
#     if num == 'quit':
#         break
#     number.append(int(num))
# print(number)

# print('What would you like to eat?')
# print('[1] Pizza')
# print('[2] Steak')
# print('[q] quit')
# choice = ''
# while choice != 'q':
#     choice = input('Enter your choice: ')
#     if choice == '1':
#         print('You chose Pizza')
#     elif choice == '2':
#         print('You chose Steak')
#     elif choice == 'q':
#         print('You chose to quit')
#     else:
#         print('Invalid choice')
# print('Thank you for choosing')

# num = []
# for i in range(10):
#     if i % 2 == 0:
#         break
#     num.append(i)
# print(num)

# def function_name(argument_1, argument_2):
# 	# Do whatever we want this function to do,
# 	#  using argument_1 and argument_2

# # Use function_name to call the function.
# function_name(value_1, value_2)

# def add_two_numbers(number_1, number_2):
#     return number_1 + number_2

# a = 5
# b = 3
# answer = add_two_numbers(a, b)
# print(answer)

# def add_two_numbers(number_1, number_2=3):
#     return number_1 + number_2

# a = 5
# answer = add_two_numbers(a)
# print(answer)

# demonstrate keyword argument
# def add_two_numbers(number_1, number_2):
#     return number_1 - number_2

# a = 5
# b = 3
# answer = add_two_numbers(number_2 = a, number_1 = b)
# print(answer)

# Accepting a sequence of arbitrary length
# def add_two_numbers(*numbers):
#     print(numbers)
#     total = 0
#     for number in numbers:
#         total += number
#     return total

# a = 5
# b = 3
# c = 10
# answer = add_two_numbers(a, b, c)
# print(answer)

# Example of accepting an arbitrary number of keyword arguments
# def example_function(arg_1, arg_2, **kwargs):
#     print('arg_1:', arg_1)
#     print('arg_2:', arg_2)
#     print('arg_3:', kwargs)

# example_function('a', 'b', value_3='c', value_4='d', value_5='e')
# f = open("test.txt",'w')  # write in text mode
# f = open("img.bmp",'r+b') # read and write in binary mode

# f = open("test.txt")
# f.close()

# with open('file.txt', 'w') as f:
# 	f.write("My hand is getting tired from head patting!")

# Python3 code for Maximum size
# square sub-matrix with all 1s

# def printMaxSubSquare(M):
#     R = len(M) # no. of rows in M[][]
#     C = len(M[0]) # no. of columns in M[][]

#     S = []
#     for i in range(R):
#       temp = []
#       for j in range(C):
#         if i==0 or j==0:
#           temp += M[i][j],
#         else:
#           temp += 0,
#       S += temp,
#     # here we have set the first row and first column of S same as input matrix, other entries are set to 0

#     # Update other entries
#     for i in range(1, R):
#         for j in range(1, C):
#             if (M[i][j] == 1):
#                 S[i][j] = min(S[i][j-1], S[i-1][j],
#                             S[i-1][j-1]) + 1
#             else:
#                 S[i][j] = 0

#     # Find the maximum entry and
#     # indices of maximum entry in S[][]
#     max_of_s = S[0][0]
#     max_i = 0
#     max_j = 0
#     for i in range(R):
#         for j in range(C):
#             if (max_of_s < S[i][j]):
#                 max_of_s = S[i][j]
#                 max_i = i
#                 max_j = j

#     print("Maximum size sub-matrix is: ")
#     for i in range(max_i, max_i - max_of_s, -1):
#         for j in range(max_j, max_j - max_of_s, -1):
#             print (M[i][j], end = " ")
#         print("")

# M = [[0, 1, 1, 0, 1],
#     [1, 1, 0, 1, 0],
#     [0, 1, 1, 1, 0],
#     [1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0]]

# M = []
# for i in range(5):
#     M.append(input().split(' '))

# for i in range(5):
#     for j in range(5):
#         M[i][j] = int(M[i][j])

# print(M)

# printMaxSubSquare(M)

# no = [str(k) for k in range(10)]
# alpha = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

# def text2keys(text):
#     text_samp = text.lower()
#     key_out = []
#     for ch in text_samp:
#         for gr in alpha:
#             if ch in gr:
#                 key_out.append(str(alpha.index(gr)) * (gr.index(ch) + 1))
#     out = " ".join(key_out)
#     return out

# def keys2text(keys):
#     chars = keys.split()
#     out = ''
#     for c in chars:
#         l = int(c[0])
#         p = len(c)
#         out += alpha[l][p-1]
#     return out

# exec(input())

# from turtle import *


# def calendar_of_2021(month):
#     speed(0)
#     pu()
#     setpos(-125, 100)
#     pd()
#     monthTxt = ["January", "February", "March", "April", "May", "June",
#                 "July", 'August', "September", "October", "November", "December"]
#     dateTxt = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
#     dateRange = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     dateStart = [5, 1, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3]
#     for i in range(2):
#         fd(250)
#         rt(90)
#         fd(30)
#         rt(90)
#     rt(90)
#     fd(30)
#     lt(90)
#     fd(125)
#     write(f"{monthTxt[month - 1]} 2022", font=("Arial", 14), align="center")
#     fd(-125)

#     for i in range(7):
#         for j in range(2):
#             fd(250 / 7)
#             rt(90)
#             fd(30)
#             rt(90)
#         fd(250 / 7)
#     fd(-250)
#     rt(90)
#     fd(30)
#     lt(90)
#     pu()
#     for i in range(7):
#         write(f"  {dateTxt[i]}", font=("Arial", 12))
#         fd(250 / 7)
#     fd(-250)
#     pd()

#     datePos = dateStart[month - 1]
#     dateCount = (0 - datePos) + 1
#     while dateCount <= dateRange[month - 1]:
#         for i in range(7):
#             if 1 <= dateCount <= dateRange[month - 1]:
#                 rt(90)
#                 fd(30)
#                 lt(90)
#                 write(f"   {dateCount}", font=("Arial", 12))
#                 lt(90)
#                 fd(30)
#                 rt(90)
#             for j in range(2):
#                 fd(250 / 7)
#                 rt(90)
#                 fd(30)
#                 rt(90)
#             fd(250 / 7)
#             dateCount += 1
#             datePos += 1
#         rt(90)
#         fd(30)
#         lt(90)
#         fd(-250)
#     ht()
#     done()

# calendar_of_2021(8)

# node = {"A": ["B", 3.4],
#         "C": ["D", 5.6],
#         "B": ["C", 4.0],
#         "D": ["E", 4.2],
#         "E": ["F", 5.5],
#         "G": ["H", 2.3],
#         "I": ["J", 3.3],
#         "F": ["G", 6.0],
#         "H": ["I", 3.9],
#         "J": [None, 0.0]}


# def find_route(start, node):
#     nodeTravelled = []
#     dist = 0
#     while True:
#         if start in node.keys() and start is not None:
#             dist += node.get(start)[1]
#             nodeTravelled += start
#             start = node.get(start)[0]
#         else:
#             break
#     return f'{nodeTravelled}, {dist:.2f} km.'


# exec(input())


# import turtle

# color1 =  'red'
# color2 = ''
# color3 = 'skyblue'
# color4 = ''

# s = turtle.getscreen()
# t = turtle.Turtle()

# def jiu():
#     t.pensize(20)

#     t.fillcolor(color1)
#     t.begin_fill()

#     t.right(90)
#     t.forward(50)
#     t.right(180)
#     t.circle(40, -180)
#     t.right(180)
#     t.forward(200)

#     t.right(180)
#     t.circle(100, -180)

#     t.backward(20)
#     t.left(15)
#     t.circle(500, -20)
#     t.backward(20)

#     t.circle(40, -180)
#     t.left(7)
#     t.backward(50)

#     t.up()
#     t.left(90)
#     t.forward(10)
#     t.right(90)
#     t.down()

#     t.right(240)
#     t.circle(50, -70)

#     t.end_fill()


# def glass():
#     t.up()

#     t.right(230)
#     t.forward(100)
#     t.left(90)
#     t.forward(20)
#     t.right(90)

#     t.down()
#     t.fillcolor(color3)
#     t.begin_fill()

#     t.right(150)
#     t.circle(90, -55)

#     t.right(180)
#     t.forward(1)
#     t.right(180)
#     t.circle(10, -65)
#     t.right(180)
#     t.forward(110)
#     t.right(180)

#     t.circle(50, -190)
#     t.right(170)
#     t.forward(80)

#     t.right(180)
#     t.circle(45, -30)

#     t.end_fill()

# def jhola():
#     t.up()
#     t.right(60)
#     t.forward(100)
#     t.right(90)
#     t.forward(75)

#     t.fillcolor(color1)
#     t.begin_fill()

#     t.down()
#     t.forward(30)
#     t.right(255)

#     t.circle(300, -30)
#     t.right(260)
#     t.forward(30)

#     t.end_fill()


# jiu()
# glass()
# jhola()
# t.ht()

# turtle.done()


# import turtle

# t = turtle.Turtle()     

# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(45)
# t.fd(200)

# turtle.done()

# sum = 5
# myList = sum([1, 2, 3, 4, 5])	# ERROR

# import turtle

# t = turtle.Turtle()

# t.setpos(-250, 250)
# t.seth(20)
# t.fd(200)
# print(t.xcor())
# print(t.heading())

# turtle.done()

# age = 18

# is_legal = 'YES' if age >= 18 else 'NO'

# print(is_legal)