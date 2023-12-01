# Write your solution here

pointValue = int(input("How many points [0-100]:"))

if pointValue < 0 or pointValue > 100:
    grade = "impossible!"
elif pointValue >= 0 and pointValue < 50: 
    grade = "fail"
elif pointValue >= 50 and pointValue <= 59:
    grade = "1"
elif pointValue >= 60 and pointValue <= 69:
    grade = "2"
elif pointValue >= 70 and pointValue <= 79:
    grade = "3"
elif pointValue >= 80 and pointValue <= 89:
    grade = "4"
elif pointValue >= 90 and pointValue <= 100:
    grade = "5"


print(f"Grade: {grade}")