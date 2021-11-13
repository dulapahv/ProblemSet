abbreviation = {"be": "b", "because": "cuz", "see": "c", "the": "da", "okay": "ok", "are": "r", "you": "u",
                "without": "w/o", "why": "y", "see you": "cu", "ate": "8", "great": "gr8", "mate": "m8",
                "wait": "w8", "later": "l8r", "tomorrow": "2mro", "for": "4", "before": "b4", "once": "1ce",
                "and": "&", "Your": "ur", "You're": "ur", "As far as I know": "afaik", "As soon as possible": "ASAP",
                "At the moment": "atm", "Be right back": "brb", "By the way": "btw", "For your Information": "FYI",
                "In my humble opinion": "imho", "In my opinion": "imo", "Laughing out loud": "lol", "Oh my god": "omg",
                "Rolling on the floor laughing": "rofl", "Talk to you later": "ttyl"}

def textese(s):
    newText = s
    for key, value in abbreviation.items():
        newText = newText.replace(key, value)
    return newText

def untextese(s):
    newText = ""
    for word in s.split():
        if word in list(abbreviation.values()):
            index = list(abbreviation.values()).index(word)
            newText += list(abbreviation)[index]
        else:
            newText += word
        newText += " "
    return newText

# print(textese("In my opinion i think you are really cute!"))
# print(untextese("imo i think u r really cute!"))