# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        if len(self.persons) == 0:
            return True
        else:
            return False
        
    def print_contents(self):
        totalHeight = 0
        for person in self.persons:
            totalHeight += person.height
        print(f'There are {len(self.persons)} persons in the room, and their combined height is {totalHeight} cm')
        for person in self.persons:
            print(f'{person.name} ({person.height} cm)')
                 
    def shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            shortestIndex = 0
            for i in range(len(self.persons)):
                if self.persons[i].height < self.persons[shortestIndex].height:
                    shortestIndex = i
            return self.persons[shortestIndex]
    
    def remove_shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            shortestPerson = self.shortest()
            for i in range(len(self.persons)):
                if self.persons[i].name == shortestPerson.name:
                    return self.persons.pop(i)



if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
