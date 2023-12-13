from random import *

def words(n: int, beginning: str):
    with open('words.txt') as words:
        wordList = []
        for line in words:
            line = line.replace("\n", "")
            if line.startswith(beginning) == True:
                wordList.append(line)
        if len(wordList) < n:
            raise ValueError
        return sample(wordList, n)

if __name__ == "__main__":
    print(words(4, "bark"))