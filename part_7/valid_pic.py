from datetime import *

def is_it_valid(pic: str):
    endCharChoices = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    controlVar = endCharChoices[int(pic[0:6] + pic[7:10]) % 31]

    if len(pic) > 11 or len(pic) < 11:
        return False
    if str(pic[6]) == '+' or str(pic[6]) == '-' or str(pic[6]) == 'A':
        ''
    else:
        print('cent identifier test trips')
        return False
    if str(pic[6]) == '+':
        year = int('18' + str(pic[4:6]))
    elif str(pic[6]) == '-':
        year = int('19' + str(pic[4:6]))
    elif str(pic[6]) == 'A':
        year = int('20' + str(pic[4:6]))
    try:
        birthDate = datetime(year, int(pic[2:4]), int(pic[0:2]))
    except:
        return False
    if int(str(pic[7:10])) > 899 or int(str(pic[7:10])) < 2:
        print(pic[7:10])
        print('personal identifier test trips')
        return False
    if str(pic[10]) not in endCharChoices or str(pic[10]) != str(controlVar):
        print('control variable test trips')
        return False
    return True

if __name__ == "__main__":
    print(is_it_valid('100400A644E'))
