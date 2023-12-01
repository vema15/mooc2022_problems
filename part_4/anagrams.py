# Write your solution here

def anagrams(word1, word2):
    sortedW1 = sorted(word1)
    sortedW2 = sorted(word2)
    overallTruth = True

    counter = 0
    while counter <= len(sortedW1)-1:
        if sortedW1[counter] == sortedW2[counter] and len(sortedW2) == len(sortedW1):
            counter += 1
            continue
        else:
            overallTruth = False
            break

    return overallTruth
if __name__ == "__main__":
    print(anagrams("tree", "three"))
    print(anagrams("python", "java"))
