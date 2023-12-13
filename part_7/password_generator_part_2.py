from string import *
from random import *


def generate_strong_password(passLen, hasNums, hasSpecial):
    while True:
        if hasNums == True and hasSpecial == True:
            hasLetters = 0
            hasNumbers = 0
            hasSpecials = 0
            passWord = ""
            acceptableSpecials = ['!', '?', '=', '+', '-', '(', ')', '#']    
            for i in range(1, passLen+1):
               randType = randint(1,3)
               if randType == 1:
                  passWord += ascii_letters[randint(0, 25)]
                  hasLetters += 1
               elif randType == 2:
                  passWord += digits[randint(0, 9)]
                  hasNumbers += 1
               elif randType == 3:
                  passWord += acceptableSpecials[randint(0, 6)]
                  hasSpecials += 1
            if hasLetters >= 1 and hasNumbers >= 1 and hasSpecials >=1:
               return passWord
            else:
               continue
        if hasNums == True and hasSpecial == False:
            hasLetters = 0
            hasNumbers = 0
            passWord = ""
            for i in range(1, passLen+1):
               randType = randint(1,2)
               if randType == 1:
                  passWord += ascii_letters[randint(0, 25)]
                  hasLetters += 1
               elif randType == 2:
                  passWord += digits[randint(0, 9)]
                  hasNumbers += 1
            if hasLetters >= 1 and hasNumbers >= 1:
               return passWord
            else:
               continue
        if hasNums == False and hasSpecial == True:
           hasLetters = 0
           hasSpecials = 0
           passWord = ""
           acceptableSpecials = ['!', '?', '=', '+', '-', '(', ')', '#']    
           for i in range(1, passLen+1):
              randType = randint(1,2)
              if randType == 1:
                 passWord += ascii_letters[randint(0, 25)]
                 hasLetters += 1
              elif randType == 2:
                 passWord += acceptableSpecials[randint(0, 6)]
                 hasSpecials += 1
           if hasLetters >= 1 and hasSpecials >= 1:
              return passWord
           else:
              continue
        if hasNums == False and hasSpecial == False:
            passWord = ""
            for i in range(1, passLen+1):
               passWord += ascii_letters[randint(0, 25)]
            return passWord


if __name__ == "__main__":
    print(generate_strong_password(5, False, False))