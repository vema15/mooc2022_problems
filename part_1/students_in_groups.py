# Write your solution here
import math


courseSize = int(input("How many students in the course?"))
desiredGroupSize = int(input("Desired group size?"))
print(f"Number of groups formed: {math.ceil(courseSize / desiredGroupSize)}")