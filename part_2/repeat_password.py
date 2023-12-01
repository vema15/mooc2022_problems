# Write your solution here

userPassWord = input("Password:")

while True:
    repeatPassWord = input("Repeat Password:")
    if userPassWord == repeatPassWord:
        print("User account created!")
        break
    else:
        print("They do not match!")