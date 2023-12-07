def getFiles():
    studInput = input("Student information: ")
    exerInput = input("Exercises completed: ")
    examInput = input("Exam points: ")
    courseInput = input("Course information: ")
    return (studInput, exerInput, examInput, courseInput)

def exConvert(exerFile):
    exDict = {}
    with open(exerFile) as exercises:
        for line in exercises:
            line = line.strip()
            sepdLine = line.split(";")
            exDict[sepdLine[0]] = []
            for item in sepdLine:
                if item == sepdLine[0]:
                   continue
                else:
                    exDict[sepdLine[0]].append(item)
    return exDict

def examConvert(examFile):
    examDict = {}
    with open(examFile) as students:
        for line in students:
            line = line.strip()
            sepdLine = line.split(";")
            examDict[sepdLine[0]] = []
            for item in sepdLine:
                if item == sepdLine[0]:
                   continue
                else:
                    examDict[sepdLine[0]].append(item)
    return examDict

def studConvert(studFile):
    studDict = {}
    with open(studFile) as students:
        for line in students:
            line = line.strip()
            sepdLine = line.split(";")
            studDict[sepdLine[0]] = []
            for item in sepdLine:
                if item == sepdLine[0]:
                   continue
                else:
                    studDict[sepdLine[0]].append(item)
    return studDict

def studExer(exerConvert, studentConvert, testConvert, courseConversion):
    open('results.txt', 'w').close()
    open('results.csv', 'w').close()
    with open(courseConversion) as courseInfo:
        lineInd = 0
        for item in courseInfo:
            item = item.replace('\n', "")
            splitLine = item.split(": ")
            if lineInd == 0:
                courseName = splitLine[1]
            else:
                studCredits = splitLine[1]
            lineInd += 1
        courseNameLen = int(len(courseName))
        studCreditsLen = int(len(str(studCredits)))
    for index in studentConvert:
        if index == 'id':
            with open('results.txt', 'a') as results:
                results.write(f'{courseName}, {studCredits} credits\n') 
                results.write(f'{(courseNameLen + studCreditsLen + 10) * "="}\n')
                results.write(f"name{' ' * (30 - len('name'))}exec_nbr{' ' * (10-(len('exec_nbr')))}exec_pts.{' ' * (10-(len('exec_pts.')))}exm_pts.{' ' * (10-(len('exm_pts.')))}tot_pts.{' ' * (10-(len('tot_pts.')))}grade{' ' * (10-(len('grade')))}\n")
                continue
        else:
            if index in exerConvert and index in testConvert:
                with open('results.csv', 'a') as resultsCSV:
                    resultsCSV.write(f'{index};{studentConvert[index][0]} {studentConvert[index][1]};')
                exerSum = 0
                examSum = 0
                for item in exerConvert[index]:
                    exerSum += int(item)
                for item in testConvert[index]:
                    examSum += int(item)
                exerPts = 0
                if exerSum >= 4 and exerSum < 8:
                    exerPts = 1
                elif exerSum >= 8 and exerSum <12:
                    exerPts = 2
                elif exerSum >= 12 and exerSum <16:
                    exerPts = 3
                elif exerSum >= 16 and exerSum <20:
                    exerPts = 4
                elif exerSum >= 20 and exerSum <24:
                    exerPts = 5
                elif exerSum >= 24 and exerSum <28:
                    exerPts = 6
                elif exerSum >= 28 and exerSum <32:
                    exerPts = 7
                elif exerSum >= 32 and exerSum <36:
                    exerPts = 8
                elif exerSum >= 36 and exerSum <40:
                    exerPts = 9
                elif exerSum >= 40:
                    exerPts = 10
                else:
                    exerPts = 0
                aggScore = exerPts + examSum
                endGrade = 0
                if aggScore <= 14:
                    endGrade = 0
                elif aggScore >= 15 and aggScore <= 17:
                    endGrade = 1
                elif aggScore >= 18 and aggScore <= 20:
                    endGrade = 2
                elif aggScore >= 21 and aggScore <= 23:
                    endGrade = 3
                elif aggScore >= 24 and aggScore <= 27:
                    endGrade = 4
                elif aggScore >= 28:
                    endGrade = 5
        with open('results.csv', 'a') as resultsCSV:
            resultsCSV.write(f'{endGrade}\n')       
        with open('results.txt', 'a') as results:
            results.write(f'{studentConvert[index][0]} {studentConvert[index][1]}{" " * (30 - (len(studentConvert[index][0]) + len(studentConvert[index][1]))-1)}{exerSum}{" " * (10-len(str(exerSum)))}{exerPts}{" " * (10-len(str(exerPts)))}{examSum}{" " * (10-len(str(examSum)))}{aggScore}{" " * (10-len(str(aggScore)))}{endGrade}{" " * (10-len(str(endGrade)))}\n')
                   
grabbedFiles = getFiles()
exerConvert = exConvert(grabbedFiles[1])
studentConvert = studConvert(grabbedFiles[0])
testConvert = examConvert(grabbedFiles[2])
courseConvert = grabbedFiles[3]
studExer(exerConvert, studentConvert, testConvert, courseConvert)