# Write your solution here

def create_tuple(x:int, y: int, z: int):
    sortList = sorted([x, y, z])
    createdTuple = (sortList[0], sortList[2], sum(sortList))
    return createdTuple

if __name__ == "__main__":
    print(create_tuple(1, 2, 3))