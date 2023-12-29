from math import *

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
        self.concat = f'{self.day}.{self.month}.{self.year}'

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'
    
    def __eq__(self, another):
        return self.concat == another.concat
    
    def __ne__(self, another):
        return self.concat != another.concat
    
    def __lt__(self, another):
        if self.year < another.year:
            return True
        elif self.year == another.year:
            if self.month < another.month:
                return True
            elif self.month == another.month:
                if self.day < another.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def __gt__(self, another):
        if self.year > another.year:
            return True
        elif self.year == another.year:
            if self.month > another.month:
                return True
            elif self.month == another.month:
                if self.day > another.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def __add__(self, another):
        totalDays = (self.year * 360) + (self.month * 30) + self.day + another
        newYear = (totalDays - (totalDays % 360)) / 360
        totalDays -= newYear * 360
        newMonth = (totalDays - (totalDays % 30)) / 30
        totalDays -= newMonth * 30
        newDay = totalDays
        return SimpleDate(int(newDay), int(newMonth), int(newYear))
    
    def __sub__(self, another):
        operand1 = (self.year * 360) + (self.month * 30) + self.day
        operand2 = (another.year * 360) + (another.month * 30) + another.day
        return abs(operand1 - operand2)

        
if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
  