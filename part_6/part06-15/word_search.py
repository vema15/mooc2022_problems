# Write your solution here
def find_words(search_term: str):
    matchList = []
    with open('words.txt') as wordDict:
        for line in wordDict:
            line = line.replace("\n", "")
            if "*" in search_term:  
                if search_term[len(search_term)-1] == "*":
                    strippedSearch = search_term[0:len(search_term)-1]
                    if line.startswith(strippedSearch) == True:
                        matchList.append(line)
                elif search_term[0] == "*":
                    strippedSearch = search_term[1:len(search_term)]
                    if line.endswith(strippedSearch) == True:
                        matchList.append(line)
            elif "." in search_term:
                periodIndices = []
                for i in range(len(search_term)):
                    if search_term[i] == ".":
                        periodIndices.append(i)
                if len(line) == len(search_term):
                    isSame = True
                    for i in range(len(line)):
                        if line[i] == search_term[i] or search_term[i] == '.':
                            isSame = True
                        else:
                            isSame = False
                            break
                    if isSame == True:
                        matchList.append(line)
                else:
                    continue
            else:
                if line == search_term:
                    matchList.append(line)
    return(matchList)
            

if __name__ == "__main__":
    print(find_words('ke*'))