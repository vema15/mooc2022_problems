def smallest_average(person1: dict, person2: dict, person3: dict):
    people = [person1, person2, person3]
    peopleAvgs = []
    indVal = 0
    for person in people:
        personSum = 0
        for key, value in person.items():
            if type(value) == int:
                personSum += value
        peopleAvgs.append([indVal, personSum/3])
        indVal += 1
    return people[sorted(peopleAvgs, key=lambda x: x[1])[0][0]]

if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    
    print(smallest_average(person1, person2, person3))