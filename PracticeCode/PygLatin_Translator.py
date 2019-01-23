print("Welcom To Pyg Lating Translator")

pyg = "ay"

original = input("Enter a word: ") #records the user's input
if len(original) > 0 and original.isalpha(): #verifies input
    word = original.lower() #turns original to lowercase
    first = word[0] #grabs first letter from original
    new_word = word[1:] + first + pyg 
    print(new_word)
elif original.isdigit():
        print("Invalid entry, please enter a WORD!")
else:
    print("empty")
