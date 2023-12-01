# Write your solution here

tempInput = int(input("What is the forecasted temperature?"))
rainYN = input("Will it rain (y/n)?")

if tempInput > 20:
    if rainYN == "yes":
        print("Wear jeans and a T-shirt")
        print("Don't forget your umbrella!")
    elif rainYN == "no":
        print("Wear jeans and a T-shirt")
elif tempInput > 10 and tempInput <= 20:
    if rainYN == "yes":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Don't forget your umbrella!")
    elif rainYN == "no":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
elif tempInput > 5 and tempInput <= 10:
    if rainYN == "yes":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
        print("Don't forget your umbrella!")
    elif rainYN == "no":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
elif tempInput <= 5:
    if rainYN == "yes":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
        print("Make it a warm coat, actually")
        print("I think gloves are in order")
        print("Don't forget your umbrella!")
    elif rainYN == "no":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
        print("Make it a warm coat, actually")
        print("I think gloves are in order")
