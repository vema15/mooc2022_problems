# Write your solution here

def dict_of_numbers():
    numDict = {}
    numConversionDict = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

    for i in range(0,100):
        if i < 21:
            numDict[i] = numConversionDict[i]
        elif i % 10 == 0:
            numDict[i] = numConversionDict[i] 
        else:
            stringNum = str(i)
            numDict[i] = numConversionDict[int(f'{stringNum[0]}' + '0')] + "-" + numConversionDict[int(f'{stringNum[1]}')]
    return numDict

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers)
