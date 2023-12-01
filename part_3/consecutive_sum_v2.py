
upperLim = int(input("Limit:"))
outFString = "The consecutive sum: "
numSum = 0
count = 1
while numSum < upperLim:
    if count != 1:
        outFString += f"+ {count} "
    else:
        outFString += f"{count} "
    numSum += count
    count += 1
outFString += f"= {numSum}"

print(outFString)
