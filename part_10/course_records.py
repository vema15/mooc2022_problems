# tee ratkaisusi tänne

class Course:
    def __init__(self):
        self._courseName = ""
        self._grade = 0
        self._credits = 0

    def __str__(self):
        return f'{self._courseName} ({self._credits} cr) grade {self._grade}'

class Courses:
    def __init__(self):
        self._course = {}

    def add_courses(self, courseName: str, courseGrade: int, courseCredits: int):
        if courseName not in self._course:
            self._course[courseName] = Course()
            self._course[courseName]._courseName = courseName
            self._course[courseName]._grade = courseGrade
            self._course[courseName]._credits = courseCredits
        else:
            if self._course[courseName]._grade < courseGrade:
                self._course[courseName]._courseName = courseName
                self._course[courseName]._grade = courseGrade
                self._course[courseName]._credits = courseCredits

    def retrieve_data(self, searchQuery: str):
        if searchQuery not in self._course:
            print("no entry for this course")
        else:
            print(self._course[searchQuery])
    
    def retrieve_statistics(self):
        completedCourses = len(self._course)
        totalCredits = 0
        aggGrade = 0
        distDict = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        }
        for key in self._course:
            totalCredits += self._course[key]._credits
            aggGrade += self._course[key]._grade
            distDict[self._course[key]._grade] += 1
        print(f"{completedCourses} completed courses, a total of {totalCredits} credits")   
        print(f"mean {float(aggGrade/completedCourses):.1f}")
        print("grade distribution")
        for key in distDict:
            print(f"{key}: {'x'*distDict[key]}")
     
class CoursesApplication:
    def __init__(self):
        self._caCourses = Courses()
    
    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
        print()

    def add_course(self):
        courseName = input("course: ")
        courseGrade = int(input("grade: "))
        courseCredits = int(input("credits: "))
        self._caCourses.add_courses(courseName, courseGrade, courseCredits)

    def retrieve_data(self):
        searchQuery = input("course: ")
        self._caCourses.retrieve_data(searchQuery)
    
    def retrieve_statistics(self):
        self._caCourses.retrieve_statistics()

    def execution(self):
        self.help()
        while True:
            userInput = input("Please choose an option: ")
            if userInput == '1':
                self.add_course()
            elif userInput == '2':
                self.retrieve_data()
            elif userInput == '3':
                self.retrieve_statistics()
            elif userInput == '0':
                break
            else:
                print("Please Enter Valid Command")

courseApp = CoursesApplication()
courseApp.execution()