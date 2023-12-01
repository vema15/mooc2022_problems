# Write your solution here
# You can test your function by calling it within the following block

def first_word(userStr):
    splitSent = userStr.split(" ")
    return splitSent[0]

def second_word(userStr):
    splitSent = userStr.split(" ")
    return splitSent[1]

def last_word(userStr):
    splitSent = userStr.split(" ")
    return splitSent[len(splitSent)-1]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))