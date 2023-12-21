# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        if self.count_numbers() == 0:
            return 0
        else:
            return sum(self.numbers)
    def average(self):
        if self.count_numbers() == 0:
            return 0
        else:
            return sum(self.numbers)/self.count_numbers()


print("Please type in integer numbers:")
allNums = NumberStats()
evenNums = NumberStats()
oddNums = NumberStats()

while True:
    userInput = int(input())
    if userInput == -1:
        print(f'Sum of numbers: {allNums.get_sum()}')
        print(f'Mean of numbers: {allNums.average()}')
        print(f'Sum of even numbers: {evenNums.get_sum()}')
        print(f'Sum of odd numbers: {oddNums.get_sum()}')
        break
    else:
        if userInput % 2 == 0:
            evenNums.add_number(userInput)
        elif userInput % 2 != 0:
            oddNums.add_number(userInput)
        allNums.add_number(userInput)
           

