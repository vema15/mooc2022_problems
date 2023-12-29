
# Write your solution here:
class Person:
    def __init__(self, name: str):
        self._name = name
        self._numbers = []
        self._address = ""

    def add_number(self, number: str):
        self._numbers.append(number)

    def add_address(self, address: str):
        self._address = address

    def name(self):
        return self._name
    
    def numbers(self):
        return self._numbers
    
    def address(self):
        if self._address == "":
            return None
        else:
            return self._address
        
    def __str__(self):
        return f'Name: {self.name()}, Numbers: {self.numbers()}, Address: {self.address()}'


class PhoneBook():
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)
    
    def add_address(self, name: str, address: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return (self.__persons[name]._numbers, self.__persons[name]._address)

    def all_entries(self):
        return self.__persons

class PhoneBookApplication():
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
    
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_entry(name)
        if numbers == None:
            print("address unknown")
            print("number unknown")
        elif numbers[0] != [] and numbers[1] == '':
            for number in numbers[0]:
                print(number)
            print('address unknown')
        elif numbers[0] == [] and numbers[1] != '':
            print('number unknown')
            print(numbers[1])
        else:
            for number in numbers[0]:
                print(number)
            print(numbers[1])
        
        #if numbers == None:
        #    print("number unknown")
        #    return
        #for number in numbers:
        #    print(number)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()