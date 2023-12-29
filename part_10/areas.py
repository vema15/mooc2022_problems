# Write your solution here!
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height
    
class Square(Rectangle):
    def __init__(self, width: int):
        self.side = width

    def area(self):
        return self.side * self.side
    
    def __str__(self):
        return f'square {self.side}x{self.side}'

if __name__ == "__main__":
    square = Square(4)
    print(square)
    print("area:", square.area())