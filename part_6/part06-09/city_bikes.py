import math

def dataOrg(filename: str):
    bikeDataBase = {}
    with open(filename) as bikeData:
        for line in bikeData:
            line = line.replace('\n', '')
            splitLine = line.split(';')
            for index in range(len(splitLine)-1):
                if index == 3:
                    bikeDataBase[splitLine[index]] = {}
                    tempName = splitLine[index]
                    break
            for index in range(len(splitLine)-1):
                if index == 0:
                    bikeDataBase[tempName]['Longitude'] = splitLine[index]
                elif index == 1:
                    bikeDataBase[tempName]['Latitude'] = splitLine[index]
                elif index == 2:
                    bikeDataBase[tempName]['FID'] = splitLine[index]
                elif index == 3:
                    continue
                elif index == 4:
                    bikeDataBase[tempName]['total_slot'] = splitLine[index]
                elif index == 5:
                    bikeDataBase[tempName]['operative'] = splitLine[index]
                elif index == 6:
                    bikeDataBase[tempName]['id'] = splitLine[index]
    return bikeDataBase

def get_station_data(filename:str):
    coordList = {}
    bikeDB = dataOrg(filename)
    for key in bikeDB:
        if key == 'name':
            continue
        else:
            coordList[key] = (float(bikeDB[key]['Longitude']), float(bikeDB[key]['Latitude']))
    return coordList

def distance(stations: dict, station1: str, station2: str):
    lonLat1 = (stations[station1][0], stations[station1][1])
    lonLat2 = (stations[station2][0], stations[station2][1])
    x_km = ((lonLat1[0] - lonLat2[0]) * 55.26)
    y_km = ((lonLat1[1] - lonLat2[1]) * 111.2)
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    distanceList = []
    for key in stations:
        for secondKey in stations:
            distanceList.append((key, secondKey, distance(stations, key, secondKey)))
    sortedList = sorted(distanceList, key=lambda x:x[2])
    return sortedList[len(sortedList)-1]
if __name__ == "__main__":
   coordDict = get_station_data('stations1.csv')
   print(greatest_distance(coordDict))

