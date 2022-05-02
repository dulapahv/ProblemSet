def caesar(txt, coded_flag=True):
    new_txt = ''
    if coded_flag:
        for char in txt:
            if char.isalpha():
                new_txt += chr((ord(char) + 3 - ord('A')) % 26 + ord('A'))
            else:
                new_txt += char
        return new_txt
    else:
        return txt

test1 = caesar("ABCDEFGHI_12345", True)
print(test1)