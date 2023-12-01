# Write your solution here

giftVal = int(input("Value of gift:"))

if giftVal < 5000:
    print("No tax!")
elif giftVal >= 5000 and giftVal < 25000:
    print(f"Amount of tax: {float(100 + ((giftVal - 5000)*0.08))} euros")
elif giftVal >= 25000 and giftVal < 55000:
    print(f"Amount of tax: {float(1700 + ((giftVal - 25000)*0.10))} euros")
elif giftVal >= 55000 and giftVal < 200000:
    print(f"Amount of tax: {float(4700 + ((giftVal - 55000)*0.12))} euros")
elif giftVal >= 200000 and giftVal < 1000000:
    print(f"Amount of tax: {float(22100 + ((giftVal - 200000)*0.15))} euros")
elif giftVal >= 1000000:
    print(f"Amount of tax: {float(142100 + ((giftVal - 1000000)*0.17))} euros")