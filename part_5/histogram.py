# Write your solution here

def histogram(userString: str):
    letters = {}
    for i in userString:
        letter = i[0]
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1
    for key in letters:
        print(key, end=" ")
        print("*"*letters[key])

if __name__ == "__main__":
    histogram("abba")