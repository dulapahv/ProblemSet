alphaNumDict = {
    'a': '2',
    'b': '22',
    'c': '222',
    'd': '3',
    'e': '33',
    'f': '333',
    'g': '4',
    'h': '44',
    'i': '444',
    'j': '5',
    'k': '55',
    'l': '555',
    'm': '6',
    'n': '66',
    'o': '666',
    'p': '7',
    'q': '77',
    'r': '777',
    's': '7777',
    't': '8',
    'u': '88',
    'v': '888',
    'w': '9',
    'x': '99',
    'y': '999',
    'z': '9999',
    ' ': ' '
}


def keys2text(text):
    num = ''
    for char in text.lower():
        num += alphaNumDict[char]
    return num


# Python3 program for the above approach
 
# Function to convert mobile numeric
# keypad sequence into its equivalent
# string
def printSentence(str1):
     
    # Store the mobile keypad mappings
    nums = [ "", "", "ABC", "DEF", "GHI", "JKL",
             "MNO", "PQRS", "TUV", "WXYZ" ]
 
    # Traverse the string str1
    i = 0
     
    while (i < len(str1)):
         
        # If the current character is
        # '.', then continue to the
        # next iteration
        if (str1[i] == '.'):
            i += 1
            continue
 
        # Stores the number of
        # continuous clicks
        count = 0
 
        # Iterate a loop to find the
        # count of same characters
        while (i + 1 < len(str1) and str1[i + 1] and
                          str1[i] == str1[i + 1]):
 
            # 2, 3, 4, 5, 6 and 8 keys will
            # have maximum of 3 letters
            if (count == 2 and ((str1[i] >= '2' and
             str1[i] <= '6') or (str1[i] == '8'))):
                break
 
            # 7 and 9 keys will have
            # maximum of 4 keys
            elif (count == 3 and (str1[i] == '7' or
                                  str1[i] == '9')):
                break
             
            count += 1
            i += 1
 
            # Handle the end condition
            if (i < len(str1)):
                break
 
        # Check if the current pressed
        # key is 7 or 9
        if (str1[i] == '7' or str1[i] == '9'):
            print(nums[ord(str1[i]) - 48][count % 4], end = "")
 
        # Else, the key pressed is
        # either 2, 3, 4, 5, 6 or 8
        else:
            print(nums[ord(str1[i]) - 48][count % 3], end = "")
             
        i += 1


print(keys2text("I love Python"))
print(printSentence("799984466666"))
