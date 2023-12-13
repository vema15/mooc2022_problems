def cheaters():
    startList = []
    endList = []
    with open('start_times.csv') as startTimes:
        for line in startTimes:
            line = line.replace("\n", "")
            startList.append(line.split(';'))
    with open('submissions.csv') as endTimes:
        for line in endTimes:
            line = line.replace("\n", "")
            endList.append(line.split(';'))
    timesDict = {}
    cheaterList = []
    for i in startList:
        if i[0] not in timesDict:
            timesDict[i[0]] = []
        for j in endList:
            if i[0] == j[0]:
                sTimeSplit = i[1].split(":")
                eTimeSplit = j[3].split(":")
                timesDict[i[0]].append(((int(sTimeSplit[0]) * 60) + int(sTimeSplit[1]) , (int(eTimeSplit[0]) * 60) + int(eTimeSplit[1])))
    for key in timesDict:
        for item in timesDict[key]:
            if item[1] - item[0] > 180:
                cheaterList.append(key)
                break
    return cheaterList
    
if __name__ == "__main__":
    cheaters()
