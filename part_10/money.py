# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self.__concat = float(f'{self.__euros}.{self.__cents:02d}')

    def __str__(self):
        if self.__cents < 10:
            return f"{self.__euros}.{self.__cents:02d} eur"
        else:
            return f"{self.__euros}.{self.__cents} eur"
        
    def __eq__(self, another):
        return self.__concat == another.__concat
            
    def __lt__(self, another):
        return self.__concat < another.__concat
    
    def __gt__(self, another):
        return self.__concat > another.__concat
        
    def __ne__(self, another):
        return self.__concat != another.__concat

    def __add__(self, another):
        return f'{(self.__concat + another.__concat):.2f} eur'

    def __sub__(self, another):
        if self.__concat - another.__concat < 0:
            raise ValueError(f"a negative result is not allowed")
        else:
            return f'{(self.__concat - another.__concat):.2f} eur'

if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1


    
    