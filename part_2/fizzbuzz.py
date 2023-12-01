# Write your solution here

userNum = int(input("Number:"))

if userNum % 3 == 0 and userNum % 5 != 0: 
    print("Fizz")
elif userNum % 5 == 0 and userNum % 3 != 0 :
    print("Buzz")
elif userNum % 3 == 0 and userNum % 5 == 0:
    print("FizzBuzz")