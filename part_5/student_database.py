# Write your solution here
def add_student(studDict, studName):
    if studName not in studDict:
        studDict[studName] = []

def add_course(studDict, studName, courseInfo):
    if studDict[studName] == [] and courseInfo[1] > 0:
        studDict[studName].append((courseInfo[0], courseInfo[1]))
    else:
        isLower = False
        for course in studDict[studName]:
            if course[0] == courseInfo[0]:
                if course[1] > courseInfo[1]:
                    isLower = True          
        if isLower == False and courseInfo[1] > 0:
            studDict[studName].append((courseInfo[0], courseInfo[1]))
    # Remove Redundancies
    index = 0
    while index <= len(studDict[studName])-1:
        if studDict[studName][index][0] == courseInfo[0]:
            if studDict[studName][index][1] < courseInfo[1]:
                studDict[studName].remove(studDict[studName][index])
                index = 0
        index+=1

def print_student(studDict, studName):
    if studName in studDict:
        courseCount = len(studDict[studName])
        if courseCount > 0:
            courseSum = 0
            for index in studDict[studName]:
                courseSum += index[1]
            courseAvg = courseSum/courseCount
            print(f'{studName}:')
            print(f' {courseCount} completed courses:')
            for index in studDict[studName]:
                print(f'  {index[0]}', end=" ")
                print(f'{index[1]}')
            print(f' average grade {float(courseAvg)}')
        else:
            print(f'{studName}:')
            print(f' no completed courses')
    else:
        print(f'{studName}: no such person in the database')

def summary(studDict: dict):
    studDictLen = len(studDict)
    print(f'students {studDictLen}')
    totalCourses = []
    for indiv in studDict:
        totalCourses.append((indiv, len(studDict[indiv])))
    sortedCourses = sorted(totalCourses, key=lambda x: x[1])
    print(f'most courses completed {sortedCourses[len(sortedCourses)-1][1]} {sortedCourses[len(sortedCourses)-1][0]}')
    courseAvgs = []
    for indiv in studDict:
        count = len(studDict[indiv])
        sum = 0   
        for i in studDict[indiv]:
            sum += i[1]
        avg = sum/count
        courseAvgs.append([indiv, avg])
    sortedCourseAvgs = sorted(courseAvgs, key=lambda x: x[1])
    print(f'best average grade {sortedCourseAvgs[len(sortedCourseAvgs)-1][1]} {sortedCourseAvgs[len(sortedCourseAvgs)-1][0]}')

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
