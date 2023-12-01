# Write your solution here

hourlyWage = float(input("Hourly Wage:"))
hoursWorked = float(input("Hours Worked:"))
dayOfWeek = input("Day of the week:")

if dayOfWeek == "Sunday":
    dailyWage = float(((2 * hourlyWage) * hoursWorked))
    print(f"Daily wages: {dailyWage} euros")
else:
    dailyWage = float((hourlyWage * hoursWorked))
    print(f"Daily wages: {dailyWage} euros")