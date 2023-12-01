# Write your solution here

while True:
    userNum = int(input("Please type in a number:"))
    if userNum <= 0: 
        print("Thanks and bye!")
        break
    product = 0
    counter = 1
    while counter <= userNum:
        if counter == 1:
            product = counter * counter
            counter+=1
            continue

        product = product * counter
        counter += 1

    print(f"The factorial of the number {userNum} is {product}")