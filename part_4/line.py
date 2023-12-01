# Write your solution here
# You can test your function by calling it within the following block

def line(userInt, userStr):
    if userStr == "":
        print("*" * userInt)
    else:
        print(userStr[0] * userInt)




if __name__ == "__main__":
    line(5, "x")