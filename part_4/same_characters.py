# Write your solution here
def same_chars(userStr, int1, int2):
    if int1 > (len(userStr)-1) or int2 > (len(userStr)-1):
        return False
    else:
        if userStr[int1] == userStr[int2]:
            return True
        else:
            return False



# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("aba", 1, 3))