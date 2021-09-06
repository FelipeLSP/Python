import math

def centroid(listCoordinates):

    xCentroid = 0
    yCentroid = 0
    listCentroid=[]
    for i in range(0, len(listCoordinates)):
        xCentroid += listCoordinates[i][0]
        yCentroid += listCoordinates[i][1]
    xCentroid = round(xCentroid / len(listCoordinates), 1)
    yCentroid = round(yCentroid / len(listCoordinates), 1)
    listCentroid.append(xCentroid)
    listCentroid.append(yCentroid)

    return listCentroid

def coordinatesDistance(listCoordinates, centroid):

    listSmaller=[]
    listBigger=[]
    listDistance=[]
    for i in range(0, len(listCoordinates)):

        distance = math.sqrt(((listCoordinates[i][0] - centroid[0]) ** 2) + ((listCoordinates[i][1] - centroid[1]) ** 2))
        listDistance.append(distance)

    temp_a = listDistance[0]
    for i in range(1, len(listDistance)):
        if  listDistance[i] < temp_a:
            temp_b = listDistance[i]
            listSmaller = listCoordinates[i]

    temp_b = listDistance[0]
    for i in range(1, len(listDistance)):
        if listDistance[i] > temp_b:
            temp_b = listDistance[i]
            listBigger = listCoordinates[i]

    return listSmaller, listBigger


#--------------------------Program Body--------------------------------------------------------------



listCoordinates = []

name = input("Type a coordinate: ")
partsA = name.split()

if name == "":
    print("No points read. So there is no centroid!!!")
    exit()

for ind in range(0,2):
    partsA[ind] = int(partsA[ind])
listCoordinates.append(partsA)
i = 1

while i >= 1:

    name = input("Type a coordinate: ")
    if name == "":
        break
    else:
        partsB = name.split()
        for ind in range(0,2):
            partsB[ind] = int(partsB[ind])
        listCoordinates.append(partsB)


listCentroid = centroid(listCoordinates)
listSmaller, listBigger = coordinatesDistance(listCoordinates, listCentroid)

print("Centroid: ", listCentroid)
print ("Closest point to the Centroid: ", listSmaller)
print ("Farthest point from the Centroid: ", listBigger)