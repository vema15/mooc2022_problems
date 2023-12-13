from string import *
from random import *

def generate_password(passLen: int):
    passWord = ""
    for i in range(passLen):
        passWord += ascii_lowercase[randint(0,25)]
    return passWord
if __name__ == "__main__":
    print(generate_password(100))
