# c =(x - n) % 26


def encripted(string, shift):
    word = ""
    for char in string:
        if char == "":
            word = word + char
        elif char.isupper():
            word = word + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            word = word + chr((ord(char) + shift - 97) % 26 + 97)
    return word


text = input("Enter the text \n")
print(text[0::])
s = int(input("Enter the shift key \n"))
print("The original text is: ", text)
print("The encrypted message is ", encripted(text, s))


def decrypt(words, shift):
    word = ""
    for char in words:
        if char == "":
            word = word + char
        elif char.isupper():
            word = word + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            word = word + chr((ord(char) - shift - 97) % 26 + 97)
    return word


text = input("Enter the text \n")
print(text[0::])
s = int(input("Enter the shift key \n"))
print("The original encrypted text is: ", text)
print("The decrypted message is ", decrypt(text, s).split())
