class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here

def names_of_students(attempts: list):
    names_list = map(lambda x:x.student_name, attempts)
    return list(names_list)

def course_names(attempts: list):
    course_name_list = list(map(lambda x:x.course_name, attempts))
    unique_list =[]
    for attempt in course_name_list:
        if attempt not in unique_list:
            unique_list.append(attempt)
    return unique_list

if __name__ == "__main__":
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in course_names([s1, s2, s3]):
        print(name)