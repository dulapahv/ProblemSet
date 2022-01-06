text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

words = text.split(" ")
length = 0
ans = ""
for word in words:
    if len(word) > length:
        ans = word
        length = len(word)
print(ans)