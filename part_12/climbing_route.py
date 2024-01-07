class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution here:
def sort_by_length(routes: list):
    return sorted(routes, key=lambda x:x.length, reverse=True)

def sort_by_difficulty(routes: list):
    route_counter = 0
    for route in routes:
        if route.grade == routes[0].grade:
            route_counter += 1
    if route_counter == len(routes):
        return sorted(routes, key=lambda x:x.length, reverse=True) 
    else:
        return sorted(routes, key=lambda x:x.grade, reverse=True)

if __name__ == "__main__":
    r1 = ClimbingRoute("Small steps", 13, "6A+")
    r2 = ClimbingRoute("Edge", 38, "6A+")
    r3 = ClimbingRoute("Bukowski", 9, "6A+")
    reply = sort_by_difficulty([r1, r2, r3])
    for replicant in reply:
        print(replicant)
