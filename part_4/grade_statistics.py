# Write your solution here
def main():
    def userEntrance():
        inputList = []
        while True:
            userInput = input("Exam points and exercises completed:")
            if userInput == "":
                return inputList
            else:
                splitItems = userInput.split(" ")
                inputList.append(splitItems)

    def covertToInt(userList):
        counter = 0
        while counter <= len(userList)-1:
            counter2 = 0
            while counter2 <= len(userList[counter])-1:
                userList[counter][counter2] = int(userList[counter][counter2])
                counter2 += 1
            counter += 1
        return userList

    def pointConverter(statsListInt):
        counter = 0
        while counter <= len(statsListInt)-1:
            if statsListInt[counter][1] >= 100 * .10 and statsListInt[counter][1] < 100 * .20:
                statsListInt[counter][1] = 1
            elif statsListInt[counter][1] >= 100 * .20 and statsListInt[counter][1] < 100 * .30:
                statsListInt[counter][1] = 2
            elif statsListInt[counter][1] >= 100 * .30 and statsListInt[counter][1] < 100 * .40:
                statsListInt[counter][1] = 3
            elif statsListInt[counter][1] >= 100 * .40 and statsListInt[counter][1] < 100 * .50:
                statsListInt[counter][1] = 4
            elif statsListInt[counter][1] >= 100 * .50 and statsListInt[counter][1] < 100 * .60:
                statsListInt[counter][1] = 5
            elif statsListInt[counter][1] >= 100 * .60 and statsListInt[counter][1] < 100 * .70:
                statsListInt[counter][1] = 6
            elif statsListInt[counter][1] >= 100 * .70 and statsListInt[counter][1] < 100 * .80:
                statsListInt[counter][1] = 7
            elif statsListInt[counter][1] >= 100 * .80 and statsListInt[counter][1] < 100 * .90:
                statsListInt[counter][1] = 8
            elif statsListInt[counter][1] >= 100 * .90 and statsListInt[counter][1] < 100:
                statsListInt[counter][1] = 9
            elif statsListInt[counter][1] == 100:
                statsListInt[counter][1] = 10
            counter += 1
        return statsListInt

    def totalPoints(convertedList):
        branchedList = []
        summedList = []
        gradeList = []
        counter = 0
        while counter <= len(convertedList)-1:
            pointSum = 0
            counter2 = 0
            while counter2 <= len(convertedList[counter])-1:
                pointSum += convertedList[counter][counter2]
                counter2 += 1
            summedList.append(pointSum)
            if convertedList[counter][0] < 10:
                gradeList.append(0)
            elif summedList[counter] >= 15 and summedList[counter] <= 17:
                gradeList.append(1)
            elif summedList[counter] >= 18 and summedList[counter] <= 20:
                gradeList.append(2)
            elif summedList[counter] >= 21 and summedList[counter] <= 23:
                gradeList.append(3)
            elif summedList[counter] >= 24 and summedList[counter] <= 27:
                gradeList.append(4)
            elif summedList[counter] >= 28 and summedList[counter] <= 30:
                gradeList.append(5)
            else:
                gradeList.append(0)
            pointSum = 0
            counter += 1
        branchedList.append(summedList)
        branchedList.append(gradeList)

        return branchedList

    def statisticsCalc(aggPoints):
       #Point Average
        sum = 0
        count = len(aggPoints[0])

        incrementer = 0
        while incrementer <= len(aggPoints[0])-1:
            sum += aggPoints[0][incrementer]
            incrementer += 1
        pointsAverage = sum/count

        #Grade Distribution
        incrementer = 0
        gradeDistList = [0,0,0,0,0,0]
        while incrementer <= len(aggPoints[1])-1:
            if aggPoints[1][incrementer] == 0:
                gradeDistList[0] += 1
            elif aggPoints[1][incrementer] == 1:
                gradeDistList[1] += 1
            elif aggPoints[1][incrementer] == 2:
                gradeDistList[2] += 1
            elif aggPoints[1][incrementer] == 3:
                gradeDistList[3] += 1
            elif aggPoints[1][incrementer] == 4:
                gradeDistList[4] += 1
            elif aggPoints[1][incrementer] == 5:
                gradeDistList[5] += 1
            incrementer += 1

        #Pass Rate
        count = 0
        incrementer = 0
        while incrementer <= len(gradeDistList)-1:
            count += gradeDistList[incrementer]
            incrementer += 1
        passPercentage = 100 - ((gradeDistList[0]/count)*100)

        statsReturn = f"Statistics:\nPoints average: {pointsAverage:.1f}\nPass percentage: {passPercentage:.1f}\nGrade distribution:\n  5: {'*' * gradeDistList[5]}\n  4: {'*' * gradeDistList[4]}\n  3: {'*' * gradeDistList[3]}\n  2: {'*' * gradeDistList[2]}\n  1: {'*' * gradeDistList[1]}\n  0: {'*' * gradeDistList[0]}"
        return statsReturn
        
    statsList = userEntrance()
    statsListInt = covertToInt(statsList)
    convertedList = pointConverter(statsListInt)
    aggPoints = totalPoints(convertedList)
    stats = statisticsCalc(aggPoints)
    return stats

print(main())
