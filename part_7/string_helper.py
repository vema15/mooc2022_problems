# Write your solution here
import math
import string
def change_case(orig_str: str):
    mod_string = []
    for letter in orig_str:
        if letter.isupper() == True:
            mod_string.append(letter.lower())
        elif letter.islower() == True:
            mod_string.append(letter.upper())
        else:
            mod_string.append(letter)
    return "".join(mod_string)

def split_in_half(orig_str: str):
    splitString = {'h1': [], 'h2': []}
    splitString['h1'].append(orig_str[0:math.ceil((len(orig_str)-1)/2)])
    splitString['h2'].append(orig_str[math.ceil((len(orig_str)-1)/2):len(orig_str)])
    return ("".join(splitString["h1"]), "".join(splitString["h2"]))

def remove_special_characters(orig_string: str):
    removedList = []
    for i in orig_string:
        if i in string.ascii_letters or i == " " or i in string.digits:
            removedList.append(i)
        continue
    return "".join(removedList)

if __name__ == "__main__":
    print(change_case("Well hello there"))
    print(split_in_half("Well hello there!"))
    print(remove_special_characters("This is a test, lets see how it goes!!!11!"))

