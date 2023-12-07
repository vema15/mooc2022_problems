# Write your solution here

def new_person(name: str, age: int):
    sepName = name.split(" ")
    if name == "" or len(sepName) < 2 or len(name) > 40 or age < 0 or age > 150:
        print("Cock")
        raise ValueError
    else:
        return (name, age)

if __name__ == "__main__":
    print(new_person('Sirkka-Liisa Virtanen-Aftenbladet-Totterstrom-Lahtiska-Vanamo-Kullervoinen', 45))