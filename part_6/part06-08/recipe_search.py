# Write your solution here
def convertRecipes(filename):
       recipeBook = {}
       with open(filename) as recipes:
           for line in recipes:
               if line[0].isupper() == True:
                   recipeBook[line.strip()] = []
                   tempKey = line.strip()
               else:
                   recipeBook[tempKey].append(line.strip())
       return recipeBook

def search_by_name(filename: str, word: str):
    recipeRef = convertRecipes(filename)
    searchList = []
    for key in recipeRef:
        tempKey = key.lower()
        if word.lower() in tempKey:
            searchList.append(key)
    return searchList

def search_by_time(filename: str, prep_time: int):
    recipeRef = convertRecipes(filename)
    searchList = []
    for key in recipeRef:
        if int(recipeRef[key][0]) <= prep_time:
            searchList.append(f'{key}, preparation time {int(recipeRef[key][0])} min')
    return searchList

def search_by_ingredient(filename: str, ingredient: str):
    recipeRef = convertRecipes(filename)
    searchList = []
    for key in recipeRef:
        if ingredient in recipeRef[key]:
            searchList.append(f'{key}, preparation time {recipeRef[key][0]} min')
    return searchList
if __name__ == "__main__":
    #print(search_by_name('recipes1.txt', 'cake'))
    #print(search_by_time('recipes1.txt', 20))
    print(search_by_ingredient('recipes1.txt', 'eggs'))