def hamming(list1, list2):

    count = 0
    differenceIndex = []

    for i in range(0, len(list1)):
        if list1[i] != list2[i]:

            differenceIndex.append(i + 1)
            count += 1

    return count, differenceIndex

def compare(k, listA, listB):

    startingPosition = []
    i = 0
    listDifference = []

    while i <= (len(listB) - len(listA)):

        listTemp = listB[i:i + len(listA)]
        result, differenceIndex = hamming(listA, listTemp)

        if  (result <= k):

            startingPosition.append(i + 1)
            listDifference.append(differenceIndex)
        i+=1


    return startingPosition, listDifference

def functionPrint(k, index, difference):

    print("Substrings with maximum distance", k, " from mofit and positions are:")

    for i in range(0, len(index)):

        print(index[i], end = " ")

        for j in range(0, len(difference[i])):

            print(difference[i][j], end = " ")

        print()



k = int(input("Type the valor of k(max value = 50): "))
motif = input("Type the motif(max characters = 50): ")
dna = input("Type the DNA(max characters = 500): ")

if k > 50 or len(motif) > 50 or len(dna) > 500:

    print("Values exceeded the maximum value!")

else:

    index, difference = compare(k, motif, dna)

    functionPrint(k, index, difference)