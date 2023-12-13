import urllib.request
import json
import math

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    read_request = my_request.read()
    splitCourse = json.loads(read_request)
    validCourseList = []
    for dict in splitCourse:
        if dict['enabled'] == True:
            sum = 0
            for i in dict['exercises']:
                sum += i
            validCourseList.append((dict['fullName'], dict['name'], dict['year'], sum))
    return validCourseList

def retrieve_course(course_name: str):
    spec_request = urllib.request.urlopen(f'https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats')
    re_request = spec_request.read()
    courseJson = json.loads(re_request)
    summaryDict = {}
    summaryDict['weeks'] = int(len(courseJson))
    maxStudents = 0
    totalHours = 0
    exerciseTotal = 0
    for dict in courseJson:
        if courseJson[dict]['students'] > maxStudents:
            maxStudents = courseJson[dict]['students']
        for key in courseJson[dict]:
            if key == 'hour_total':
                totalHours += courseJson[dict]['hour_total']
            if key == 'exercise_total':
                exerciseTotal += courseJson[dict]['exercise_total']
    summaryDict['students'] = maxStudents
    summaryDict['hours'] = totalHours
    summaryDict['hours_average'] = math.floor(totalHours/maxStudents) 
    summaryDict['exercises'] = exerciseTotal
    summaryDict['exercises_average'] = math.floor(exerciseTotal/maxStudents)
    return summaryDict

if __name__ == "__main__":
    retrieve_course('docker2019')
