def anti_vowel(text):
    word = []
    string = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    for character in text:
        word.append(character)
        if character in string:
            word.remove(character)
        text = word
    return"".join(text)

print (anti_vowel("Raul"))
