import string

def most_common_words(filename: str, lower_limit: int):
    list_of_words = []
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            line = line.split(" ")
            for word in line:
                list_of_words.append("".join([letter for letter in word if letter not in string.punctuation]))
    return {word : list_of_words.count(word) for word in list_of_words if list_of_words.count(word) >= lower_limit}

if __name__ == "__main__":
    most_common_words('comprehensions.txt', 3)
