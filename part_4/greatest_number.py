# Write your solution here
# You can test your function by calling it within the following block

def greatest_number(a, b, c):
    if a == b and b == c:
        return a
    elif a < b or (a == b and b != c):
        if b < c:
            return c
        else: 
            return b
    elif a > b or (a == b and b != c):
        if a < c:
            return c
        else: 
            return a



if __name__ == "__main__":
    greatest = greatest_number(1, 1, -100)
    print(greatest)