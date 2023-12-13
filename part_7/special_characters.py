import string
def separate_characters(my_string: str):
    asciiString = ""
    asciiPunc = ""
    rest = ""
    asciiChars = string.ascii_letters
    punctuation = string.punctuation
    for i in my_string:
        if i in asciiChars:
            asciiString+=i
        elif i in punctuation:
            asciiPunc+=i
        else:
            rest+=i

    return (asciiString, asciiPunc, rest)


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])


