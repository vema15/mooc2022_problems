# WRITE YOUR SOLUTION HERE:

class LotteryNumbers:
    def __init__(self, week: int, num_list: list):
        self.week = week
        self.num_list = num_list

    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.num_list])
    
    def hits_in_place(self, numbers: list):
        return [number if number in self.num_list else -1 for number in numbers]
    
if __name__ == "__main__":
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))