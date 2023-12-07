# Write your solution here

def filter_incorrect():
    open('correct_numbers.csv', 'w').close()
    lottoNumDict = {}
    with open('lottery_numbers.csv') as lottoNums:
        for line in lottoNums:
            line = line.replace("\n", "")
            sepLine = line.split(";")
            iterKey = sepLine[0]
            lottoNumDict[iterKey] = []
            sepNums = sepLine[1].split(',')
            for i in sepNums:
                try:
                    lottoNumDict[iterKey].append(int(i))
                except ValueError:
                    continue
    numFilt = {}
    for key, value in lottoNumDict.items():
        if len(value) != 7:
            continue
        contVal = True
        for i in value:
            if (i > 39 or i < 1) or value.count(i) > 1:
                contVal = False
                break
        if contVal == False:
            continue
        else:
            numFilt[key] = value
    for key, value in numFilt.items():
        splitKey = key.split(" ")
        try:
            if int(splitKey[1]) != ValueError:
                with open("correct_numbers.csv", 'a') as correctNumbers:
                    correctNumbers.write(f'{key};')
                    for i in range(len(value)):
                        if i == 6:
                            correctNumbers.write(f'{value[i]}')
                        else:
                            correctNumbers.write(f'{value[i]},')
        except:
            continue
        with open('correct_numbers.csv', 'a') as correctNumbers:
            correctNumbers.write('\n')

if __name__ == "__main__":
    filter_incorrect()