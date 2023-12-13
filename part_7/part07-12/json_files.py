import json

def print_persons(filename: str):
    with open(filename) as jsonFile:
        unpackedJson = jsonFile.read()
    
    persons = json.loads(unpackedJson)
    for dict in persons:
        for key in dict:
            if key == "hobbies":
                print('(', end='')
                for i in range(len(dict[key])):
                    if i == len(dict[key])-1:
                        print(dict[key][i], end="")
                        continue
                    print(f'{dict[key][i]},', end=" ")
                print(')')
                continue
            if key == 'age':
                print(f'{dict[key]} years ', end="")
                continue
            print(dict[key], end=" ")


if __name__ == "__main__":
    print_persons('file1.json')