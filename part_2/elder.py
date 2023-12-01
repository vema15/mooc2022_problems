# Write your solution here

person1Name = input("Name:") 
person1Age = int(input("Age:"))
person2Name = input("Name:") 
person2Age = int(input("Age:"))

if person1Age > person2Age:
    print(f"The elder is {person1Name}")
elif person1Age < person2Age:
    print(f"The elder is {person2Name}")
else: 
    print(f"{person1Name} and {person2Name} are the same age")