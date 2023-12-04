# Write your solution here

def times_ten(start_index: int, end_index: int):
    z = {}
    for i in range(start_index, end_index+1):
        z[i] = i*10
    return z
if __name__ == "__main__":
    d = times_ten(1,3)
    print(d)