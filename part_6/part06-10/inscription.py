# Write your solution here

userName = input("Whom should I sign this to: ")
userFile = input("Where shall I save it: ")

with open(userFile, "w") as userFile:
    userFile.write(f"Hi {userName}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")


    