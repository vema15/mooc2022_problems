# write your solution here
def getFiles():
    studInput = input("Student information: ")
    exerInput = input("Exercises completed: ")
    return (studInput, exerInput)


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

def studExer(exerConvert, studentConvert):
    gradeList = {}
    for index in studentConvert:
        if index == 'id':
            continue
        else:
            if index in studentConvert:
                sumGrade = 0
                for item in exerConvert[index]:
                    sumGrade += int(item)
                gradeList[f'{studentConvert[index][0]} {studentConvert[index][1]}'] = sumGrade
    for key in gradeList:
        print(f'{key} {gradeList[key]}')


grabbedFiles = getFiles()
exerConvert = exConvert(grabbedFiles[1])
studentConvert = studConvert(grabbedFiles[0])
studExer(exerConvert, studentConvert)

    
    
    