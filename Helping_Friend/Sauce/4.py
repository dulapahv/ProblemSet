# For test-run (Modified)
import sys

# Skeleton code
class analysedText:
    ### BEGIN SOLUTION
    def __init__ (self, text):
        self.text = text.lower().split(" ")
        for i in range(len(self.text)):
            self.text[i] = self.text[i].strip("?!.,")
        
    def fmtText(self):
        return " ".join(self.text)

    def freqAll(self):
        freq = {}
        for i in self.text:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        return freq

    def freqOf(self,word):
        freq = 0
        for i in self.text:
            if i == word:
                freq += 1
        return freq

    ### END SOLUTION

sampleMap = {'love': 3, 'beams': 1, 'story': 1, 'the': 2, 'place': 1, 'starting': 1, 'bricks': 1, 'a': 5, \
             'always': 1, 'even': 1, 'feels': 2, 'created': 1, 'magic': 1, 'to': 2, 'friends': 1, 'belong': 1, \
             'dreams': 2, 'is': 8, 'memories': 1, 'hopes': 1, 'laughter': 1, 'good': 1, 'that': 1, 'house': 2, \
             'begins': 1, 'come': 1, 'it': 2, 'our': 1, 'and': 5, 'i': 1, 'about': 1, 'of': 4, 'not': 1, \
             'ends': 1, 'where': 2, 'true': 1, 'resides': 1, 'what': 1, 'my': 1, 'are': 1, 'made': 2, 'back': 1, \
             'leave': 1, 'home': 8, 'thing': 1, 'never': 1, 'meaning': 1, 'better': 1, 'hope': 1}
    
def testMsg(passed):
    if passed:
       return '   Test Passed'
    else :
       return '   Test Failed'

print("Constructor: ")
try:
    samplePassage = analysedText("What is a true meaning of home? A House Is Not a Home! A house is made of bricks and beams. A home is made of hopes and dreams. Home is where our story begins. Home is the starting place of love, hope and dreams. The magic thing about home is that it feels good to leave, and it feels even better to come back. Home is where love resides, memories are created, friends always belong, and laughter never ends. I love my home.")
    print(testMsg(samplePassage.fmtText() == "what is a true meaning of home a house is not a home a house is made of bricks and beams a home is made of hopes and dreams home is where our story begins home is the starting place of love hope and dreams the magic thing about home is that it feels good to leave and it feels even better to come back home is where love resides memories are created friends always belong and laughter never ends i love my home"))
except:
    print("Error detected. Recheck your function " )

print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print("Error detected. Recheck your function " )
    
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))
except:
    print("Error detected. Recheck your function  " )
