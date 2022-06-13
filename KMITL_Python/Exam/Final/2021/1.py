def find_word_positions(word, list_of_words):
    pos = []
    for index, element in enumerate(list_of_words):
        if element.lower() == word.lower():
            pos.append(index)
    if pos:
        return pos
    else:
        return 0

print(find_word_positions("Python",["python","java", "c","PYTHON","Prolog"]))
print(find_word_positions("iOS",["Windows","macOS","Linux"]))