import random
# Write your solution here:

def word_generator(characters: str, length: int, amount: int):
    for i in range(amount):
        rand_chars = []
        for j in range(length):
            rand_chars.append(characters[random.randint(0,len(characters)-1)])
        yield "".join(rand_chars)

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)