# Write your solution here

userTempInput = float(input("Please type in a temperature (F):"))
celsConversion = float((userTempInput - 32) * (5/9))

if celsConversion >= 0:
    print(f"{userTempInput} degrees Fahrenheit equals {celsConversion} degrees Celsius")
elif celsConversion < 0:
    print(f"{userTempInput} degrees Fahrenheit equals {celsConversion} degrees Celsius")
    print("Brr! It's cold in here!")