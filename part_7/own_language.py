import string
import operator

def run(gathered_code: list):
    numList = []
    for i in range(10000000):
        numList.append(str(i))
    resultList = []
    locationDict = {}
    currRam = {}
    splitCode = []
    for i in range(len(gathered_code)):
        iSplit = gathered_code[i].split(" ")
        if iSplit[0][len(iSplit[0])-1] == ":":
            locationDict[iSplit[0][0:len(iSplit[0])-1]] = i
    for letter in string.ascii_uppercase:
        currRam[letter] = 0
    for i in gathered_code:
        splitCode.append(i.split(" "))
    i = 0
    j = len(splitCode)-1

    while i <= j:
        if splitCode[i][0] == "END":
            return resultList
        elif splitCode[i][0] == "PRINT":
            if splitCode[i][1] in string.ascii_uppercase:
                resultList.append(int(currRam[splitCode[i][1]]))
            else:
                resultList.append(int(splitCode[i][1]))
            i += 1
            continue
        elif splitCode[i][0] == "MOV":
            if splitCode[i][2] in string.ascii_uppercase:
                currRam[splitCode[i][1]] = int(currRam[splitCode[i][2]])
            else:
                currRam[splitCode[i][1]] = int(splitCode[i][2])
            i += 1
            continue
        elif splitCode[i][0] == "ADD":
            if splitCode[i][2] in string.ascii_uppercase:
                currRam[splitCode[i][1]] = int(currRam[splitCode[i][1]]) + int(currRam[splitCode[i][2]])
            else:
                currRam[splitCode[i][1]] = int(currRam[splitCode[i][1]]) + int(splitCode[i][2])
            i += 1
            continue
        elif splitCode[i][0] == "SUB":
            if splitCode[i][2] in string.ascii_uppercase:
                currRam[splitCode[i][1]] = int(currRam[splitCode[i][1]]) - int(currRam[splitCode[i][2]])
            else:
                currRam[splitCode[i][1]] = int(currRam[splitCode[i][1]]) - int(splitCode[i][2])
            i += 1
            continue
        elif splitCode[i][0] == "MUL":
            if splitCode[i][2] in string.ascii_uppercase:
                currRam[splitCode[i][1]] = int(currRam[splitCode[i][1]]) * int(currRam[splitCode[i][2]])
            else:
                currRam[splitCode[i][1]] = int(currRam[splitCode[i][1]]) * int(splitCode[i][2])
            i += 1
            continue
        elif splitCode[i][0] == "JUMP":
            i = locationDict[splitCode[i][1]]+1
            continue
        elif splitCode[i][0][len(splitCode[i][0])-1] == ":":
            i += 1
            continue
        elif splitCode[i][0] == "IF":
            if splitCode[i][1] in string.ascii_uppercase and splitCode[i][3] in string.ascii_uppercase:
                ops = {
                "==": operator.eq(currRam[splitCode[i][1]], currRam[splitCode[i][3]]),
                "!=": operator.ne(currRam[splitCode[i][1]], currRam[splitCode[i][3]]),
                ">=": operator.ge(currRam[splitCode[i][1]], currRam[splitCode[i][3]]),
                ">": operator.gt(currRam[splitCode[i][1]], currRam[splitCode[i][3]]),
                "<=": operator.le(currRam[splitCode[i][1]], currRam[splitCode[i][3]]),
                "<": operator.lt(currRam[splitCode[i][1]], currRam[splitCode[i][3]])
                }
                if ops[splitCode[i][2]] == True:
                    i = locationDict[splitCode[i][5]]
                    continue
                else:
                    i += 1
                    continue
            elif str(splitCode[i][1]) in string.ascii_uppercase and str(splitCode[i][3]) in numList:
                ops = {
                "==": operator.eq(currRam[splitCode[i][1]],int(splitCode[i][3])),
                "!=": operator.ne(currRam[splitCode[i][1]], int(splitCode[i][3])),
                ">=": operator.ge(currRam[splitCode[i][1]], int(splitCode[i][3])),
                ">": operator.gt(currRam[splitCode[i][1]], int(splitCode[i][3])),
                "<=": operator.le(currRam[splitCode[i][1]], int(splitCode[i][3])),
                "<": operator.lt(currRam[splitCode[i][1]], int(splitCode[i][3]))
                }
                if ops[splitCode[i][2]] == True:
                    i = locationDict[splitCode[i][5]]
                    continue
                else:
                    i += 1
                    continue
            elif splitCode[i][1] in numList and splitCode[i][3] in string.ascii_uppercase:
                ops = {
                "==": operator.eq(int(splitCode[i][1]), currRam[splitCode[i][3]]),
                "!=": operator.ne(int(splitCode[i][1]), currRam[splitCode[i][3]]),
                ">=": operator.ge(int(splitCode[i][1]), currRam[splitCode[i][3]]),
                ">": operator.gt(int(splitCode[i][1]), currRam[splitCode[i][3]]),
                "<=": operator.le(int(splitCode[i][1]), currRam[splitCode[i][3]]),
                "<": operator.lt(int(splitCode[i][1]), currRam[splitCode[i][3]])
                }
                if ops[splitCode[i][2]] == True:
                    i = locationDict[splitCode[i][5]]
                    continue
                else:
                    i += 1
                    continue
            elif splitCode[i][1] in numList and splitCode[i][3] in numList:
                ops = {
                "==": operator.eq(int(splitCode[i][1]),int(splitCode[i][3])),
                "!=": operator.ne(int(splitCode[i][1]), int(splitCode[i][3])),
                ">=": operator.ge(int(splitCode[i][1]), int(splitCode[i][3])),
                ">": operator.gt(int(splitCode[i][1]), int(splitCode[i][3])),
                "<=": operator.le(int(splitCode[i][1]), int(splitCode[i][3])),
                "<": operator.lt(int(splitCode[i][1]), int(splitCode[i][3]))
                }
                if ops[splitCode[i][2]] == True:
                    i = locationDict[splitCode[i][5]] 
                    continue
                else:
                    i += 1
                    continue
            else:
                i += 1
    return resultList


if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)
