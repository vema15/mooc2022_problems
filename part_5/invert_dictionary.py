def invert(dictionary: dict):
    count = 0
    while count <= len(dictionary)-1:
        for key in dictionary:
            tempKey = key
            key = dictionary[key]
            dictionary[key] = tempKey
            dictionary.pop(tempKey)
            break
        count+=1


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
