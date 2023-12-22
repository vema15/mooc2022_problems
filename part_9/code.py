# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f'{self.__name} ({self.__weight} kg)'
    
class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item: Item):
        totalWeight = 0
        for i in range(len(self.__items)):
            totalWeight += self.__items[i].weight()
        if (totalWeight + item.weight()) < self.__max_weight:
            self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(item)
    
    def weight(self):
        totalWeight = 0
        for i in range(len(self.__items)):
            totalWeight += self.__items[i].weight()
        return totalWeight
    
    def heaviest_item(self):
        if len(self.__items) == 0:
            return None
        else:
            heaviestWeight = 0
            heaviestItem = None
            for i in range(len(self.__items)):
                if self.__items[i].weight() > heaviestWeight:
                    heaviestWeight = self.__items[i].weight()
                    heaviestItem = self.__items[i]
            return heaviestItem
        
    def __str__(self):
        if len(self.__items) == 1:
            return f'{len(self.__items)} item ({self.weight()} kg)'

        else:
            return f'{len(self.__items)} items ({self.weight()} kg)'

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__total_weight = 0
        self.__cargo_hold = []

    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() + self.__total_weight < self.__max_weight:
            self.__cargo_hold.append(suitcase)
            self.__total_weight += suitcase.weight()

    def __str__(self):
        if len(self.__cargo_hold) == 1:
            return f'{len(self.__cargo_hold)} suitcase, space for {self.__max_weight - self.__total_weight} kg'
        else:
            return f'{len(self.__cargo_hold)} suitcases, space for {self.__max_weight - self.__total_weight} kg'
    
    def print_items(self):
        for suitcase in self.__cargo_hold:
            suitcase.print_items()

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()