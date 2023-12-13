from datetime import *

fileInput = input('Filename: ')
open(fileInput, 'w').close()
dateInput = input('Starting date: ').split(".")
startDate = datetime(int(dateInput[2]), int(dateInput[1]), int(dateInput[0]))
dayNumInput = int(input("How many days: "))
endDate = startDate + timedelta(days = dayNumInput-1)
screenTimeDict = {}
print("Please type in screen time in minutes on each day (TV computer mobile):")
for i in range(dayNumInput):
    todaysDate = startDate + timedelta(days=int(i))
    tDFormatted = todaysDate.strftime("%d.%m.%Y")
    dailyScreenTime = list(map(int, input(f'Screen time {todaysDate}: ').split(" ")))
    screenTimeDict[tDFormatted] = dailyScreenTime

with open(fileInput, 'a') as lateJune:
    lateJune.write(f"Time period: {startDate.strftime('%d.%m.%Y')}-{endDate.strftime('%d.%m.%Y')}\n")
    totalMinutes = 0
    for key in screenTimeDict:
        totalMinutes += sum(screenTimeDict[key])
    lateJune.write(f'Total minutes: {totalMinutes}\n')
    lateJune.write(f'Average minutes: {float(totalMinutes/dayNumInput)}\n')
    for key in screenTimeDict:
        lateJune.write(f'{key}: {screenTimeDict[key][0]}/{screenTimeDict[key][1]}/{screenTimeDict[key][2]}\n')
    print(f"Data stored in file {fileInput}")

