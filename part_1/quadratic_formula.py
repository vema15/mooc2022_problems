# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

x1 = (-b + sqrt(b * b - 4* a * c))/(2 * a)
x2 = (-b - sqrt(b * b - 4* a * c))/(2 * a)

print(f"The roots are {x1} and {x2}.")
