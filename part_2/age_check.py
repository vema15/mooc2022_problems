# Write your solution here

userAge = int(input("What is your age?"))

if userAge >= 5:
    print(f"Ok, you're {userAge} years old")
elif userAge < 5 and userAge >= 0:
    print("I suspect you can't write quite yet...")
elif userAge < 0: 
    print("That must be a mistake")