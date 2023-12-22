# WRITE YOUR SOLUTION HERE:

class Car:
    def __init__(self):
        self.__amount = 0
        self.__odometer = 0

    def fill_up(self):
        self.__amount = 60

    def drive(self, km: int):
        if km <= self.__amount:
            self.__odometer += km
            self.__amount -= km
        else: 
            self.__odometer += self.__amount
            self.__amount -= self.__amount

    def __str__(self):
        return f'Car: odometer reading {self.__odometer} km, petrol remaining {self.__amount} litres'


if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)