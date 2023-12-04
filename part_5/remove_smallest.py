# Write your solution here

def remove_smallest(numbers: list):
    sortedNumbers = sorted(numbers)
    for item in numbers:
        if item == sortedNumbers[0]:
            numbers.remove(item)
if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
