class Clock:
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def tick(self):
        if self.hour == 23 and self.minute == 59 and self.second == 59:
            self.hour = 0
            self.minute = 0
            self.second = 0
        elif self.minute == 59 and self.second == 59:
            self.hour += 1
            self.minute = 0
            self.second = 0
        elif self.second == 59:
            self.minute += 1
            self.second = 0
        else:
            self.second += 1

    def set(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute
        self.second = 0

    def __str__(self) -> str:
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
    

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)
        