# Write your solution here
attemptCount = 0
correctPin = int(4321) 

while True:
    userPinAttempt = int(input("PIN:"))

    if userPinAttempt != correctPin:
        print("Wrong")
        attemptCount += 1
    elif userPinAttempt == correctPin:
        attemptCount += 1
        break

if attemptCount == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attemptCount} attempts")