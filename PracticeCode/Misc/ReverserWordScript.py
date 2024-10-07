def reverse(word):
    x = ''
    for letter in range(len(str(word))):
        letter -= 1
        x.append(letter)
        return ''.join(x)
