# Write your solution here

cafeteriaFrequencyWk = float(input("How many times a week do you eat at the student cafeteria?"))
priceOfLunch = float(input("What is the price of a typical student lunch?"))
groceryCostWk = float(input("How much money do you spend on groceries in a week?"))
print("Average food expenditure:")
print(f"Daily: {((cafeteriaFrequencyWk * priceOfLunch) + groceryCostWk)/7} euros")
print(f"Weekly: {(cafeteriaFrequencyWk * priceOfLunch) + groceryCostWk} euros")