# WRITE YOUR SOLUTION HERE:

class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__obsList = []

    def add_observation(self, observation: str):
        if observation == "":
            raise ValueError
        else:
            self.__obsList.append(observation)
    
    def latest_observation(self):
        if len(self.__obsList) == 0:
            return ""
        else:
            return self.__obsList[len(self.__obsList)-1]
    
    def number_of_observations(self):
        return len(self.__obsList)
    
    def __str__(self):
        return f"{self.__name}, {len(self.__obsList)} observations"
    
if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())
    
    station.add_observation("Thunderstorm")
    print(station.latest_observation())
    
    print(station.number_of_observations())
    print(station)    


