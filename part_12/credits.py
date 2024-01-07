from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(courses: list):
    return reduce(lambda reduce_sum, item: reduce_sum + item, list(map(lambda x:x.credits, courses)))

def sum_of_passed_credits(courses: list):
    return reduce(lambda specific_sum, thing: specific_sum + thing, list(map(lambda x:x.credits ,filter(lambda x:x.grade > 0, courses))))

def average(courses: list):
    return reduce(lambda summation, iter: summation + iter, list(map(lambda x:x.grade, (list(filter(lambda x: x.grade > 0, courses))))))/len((list(map(lambda x:x.grade, (list(filter(lambda x: x.grade > 0, courses)))))))



if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)
