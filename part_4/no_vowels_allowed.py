# Write your solution here

def no_vowels(userString):
    counter = 0
    
    while counter <= len(userString)-1:
        if userString[counter] == 'a' or userString[counter] == 'i' or userString[counter] == 'o' or userString[counter] == 'u' or userString[counter] == 'e':
            userString = userString.replace(userString[counter], "")
        else:
            counter += 1
    return userString


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))