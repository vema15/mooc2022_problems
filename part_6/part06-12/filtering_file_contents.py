# Write your solution here
def filter_solutions():
    open('correct.csv', 'w').close()
    open('incorrect.csv', 'w').close()
    readCSV = []
    with open('solutions.csv') as solutions:
        for line in solutions:
           lineList = []
           line = line.replace("\n", "")
           splitLine = line.split(";")
           for item in splitLine:
                lineList.append(item)
           readCSV.append(lineList) 
    for item in readCSV:
        for index in range(len(item)-1):
            if index == 1:
                if "+" in item[index]:
                    splitInd = item[index].split("+")
                    if int(splitInd[0]) + int(splitInd[1]) == int(item[2]):
                        with open('correct.csv', 'a') as correct:
                            correct.write(f'{item[0]};{item[1]};{item[2]}\n')
                    else:
                        with open('incorrect.csv', 'a') as incorrect:
                            incorrect.write(f'{item[0]};{item[1]};{item[2]}\n')
                elif "-" in item[index]:
                     splitInd = item[index].split("-")
                     if int(splitInd[0]) - int(splitInd[1]) == int(item[2]):
                        with open('correct.csv', 'a') as correct:
                            correct.write(f'{item[0]};{item[1]};{item[2]}\n')
                        break
                     else:
                         with open('incorrect.csv', 'a') as incorrect:
                             incorrect.write(f'{item[0]};{item[1]};{item[2]}\n')
                         break
            
if __name__ == "__main__":
    filter_solutions()
