# Write your solution here
layer = int(input("Layers:"))
rowColLen = 1 + (layer-1) * 2
layersConv = {
    1:'A',
    2:'B',
    3:'C',
    4:'D',
    5:'E',
    6:'F',
    7:'G',
    8:'H',
    9:'I',
    10:'J',
    11:'K',
    12:'L',
    13:'M',
    14:'N',
    15:'O',
    16:'P',
    17:'Q',
    18:'R',
    19:'S',
    20:'T',
    21:'U',
    22:'V',
    23:'W',
    24:'X',
    25:'Y',
    26:'Z'
}
layerList = []
for i in range(layer):
        layerList.append([])
        for j in range(layer-1):
            if layersConv[layer-j] < layersConv[i+1]:
                layerList[i].append(layersConv[i+1])
            else:
                layerList[i].append(layersConv[layer-j])
        layerList[i].append(layersConv[i+1])
        for j in reversed(range(layer-1)):
            if layersConv[layer-j] < layersConv[i+1]:
                layerList[i].append(layersConv[i+1])
            else:
                layerList[i].append(layersConv[layer-j])

for i in reversed(range(len(layerList))):
    for j in layerList[i]:
        print(j, end="")
    print()
for i in range(len(layerList)):
    if i == 0:
        continue
    for j in layerList[i]:
        print(j, end="")
    print()    