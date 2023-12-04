# Write your solution here

def find_movies(database: list, search_term: str):
    lowerSearch = search_term.lower()
    dupeList = []
    searchedList = []
    for i in database:
        dupeList.append(i)    
    for indexVal in dupeList:
        for key in indexVal:
            if type(indexVal[key]) == str: 
                indValPlaceHolder = indexVal[key]
                indexVal[key] = indexVal[key].lower()
                if lowerSearch in indexVal[key]:
                    indexVal[key] = indValPlaceHolder
                    searchedList.append(indexVal)
                    break
    return searchedList
   
if __name__ == "__main__":
    database = [
        {"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
        {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
        {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}
        ]

    my_movies = find_movies(database, "Python")
    print(my_movies)